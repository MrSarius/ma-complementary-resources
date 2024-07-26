import time
import json
import threading
import psutil
import pandas as pd
import requests
import random
import subprocess

from Parser import BASE_PATH


def clean(system_manager_url, net_mananger_url):
    delete_all_apps(system_manager_url)
    delete_all_ebpf_modules(net_mananger_url)
    time.sleep(5)


def get_random_string(length):
    # choose from all lowercase letter
    result_str = ''.join(random.choice('qwertyuiopasdfghjklzxcvbnm') for i in range(length))
    return result_str


def getlogin(system_manager_url: str):
    url = "http://" + system_manager_url + "/api/auth/login"
    credentials = {
        "username": "Admin",
        "password": "Admin"
    }
    r = requests.post(url, json=credentials)
    return r.json()["token"]


def register_app(system_manager_url: str, deployment_descriptor):
    token = getlogin(system_manager_url)

    # print(deployment_descriptor)
    head = {'Authorization': "Bearer " + token}
    url = "http://" + system_manager_url + "/api/application"
    deployment_descriptor["applications"][0]["application_namespace"] = get_random_string(5)
    resp = requests.post(url, headers=head, json=deployment_descriptor)

    if resp.status_code == 200:
        json_resp = json.loads(resp.json())
        print(json_resp)
        for app in json_resp:
            if app.get("application_name") == "test1":
                json_resp = app
                return json_resp.get("applicationID"), json_resp.get("microservices")
    print(resp)
    return "", []


def undeploy_all(app_id, system_manager_url: str):
    print("\t Asking Undeployment")
    token = getlogin(system_manager_url)
    url = "http://" + system_manager_url + "/api/application/" + str(app_id)
    resp = requests.delete(url, headers={'Authorization': 'Bearer {}'.format(token)})
    time.sleep(10)
    pass


def scale_up_service(amount, microserviceid, system_manager_url):
    print("\t Asking scaleup of n.", amount, " insances of ", microserviceid)
    token = getlogin(system_manager_url)
    for i in range(int(amount)):
        url = "http://" + system_manager_url + "/api/service/" + microserviceid + "/instance"
        resp = requests.post(url, headers={'Authorization': 'Bearer {}'.format(token)})
        time.sleep(1)
    pass


def delete_all_apps(system_manager_url: str):
    token = getlogin(system_manager_url)
    url = "http://" + system_manager_url + "/api/services"
    resp = requests.get(url, headers={'Authorization': 'Bearer {}'.format(token)})
    if resp.status_code == 200:
        json_resp = json.loads(resp.json())
        print(json_resp)
        for app in json_resp:
            url = "http://" + system_manager_url + "/api/application/" + app.get("applicationID")
            r = requests.delete(url, headers={'Authorization': 'Bearer {}'.format(token)})
            print(r)
            print("Waiting undeployment cooldown")
            time.sleep(2)


def check_deployment(microservices, system_manager_url: str):
    token = getlogin(system_manager_url)
    head = {'Authorization': 'Bearer {}'.format(token)}
    clientip = "0.0.0.0"
    for microservice in microservices:
        url = "http://" + system_manager_url + "/api/service/" + microservice
        resp = requests.get(url, headers={'Authorization': 'Bearer {}'.format(token)})
        if resp.status_code == 200:
            json_resp = json.loads(resp.json())
            instances = json_resp["instance_list"]
            if instances is not None:
                for instance in instances:
                    try:
                        if json_resp["microservice_name"] == "client":
                            clientip = instance["publicip"]
                        if instance["status"] != "RUNNING":
                            return False, str(json_resp["microservice_name"])
                    except:
                        return False, str(json_resp["microservice_name"])
            else:
                return False, "No instances"
    return True, clientip


def delete_all_ebpf_modules(net_manager_url):
    url = "http://" + net_manager_url + "/ebpf"

    payload = {}
    headers = {}

    response = requests.request("DELETE", url, headers=headers, data=payload)

    if response.status_code != 200:
        return False

    return True


def enable_ebpf_proxy(net_manager_url: str) -> bool:
    url = "http://" + net_manager_url + "/ebpf"
    payload = json.dumps({
        "name": "proxy",
        "config": {}
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code != 200:
        return False

    return True


class CpuRamCollector:
    thread = None
    cpu_ram_info = {
        "idle": [],
        "load": [],
        "cleanup": []
    }
    collection_state = "idle"
    thread_running = False
    sleep = 0.5

    def set_collection_state(self, state: str):
        if state == "idle" or state == "load" or state == "cleanup":
            self.collection_state = state
        else:
            print("Error: Invalid State")

    def clear_collection(self):
        self.cpu_ram_info = {
            "idle": [],
            "load": [],
            "cleanup": []
        }

    def collect_cpu_ram(self):
        self.clear_collection()
        while self.thread_running:
            current_timestamp = int(time.time() * 1000)
            cpu_usage = psutil.cpu_percent(interval=0)
            used_ram_kbit = psutil.virtual_memory().used * 8 / 1024
            self.cpu_ram_info[self.collection_state].append((current_timestamp, cpu_usage, used_ram_kbit))
            time.sleep(self.sleep)

    def start_collecting_cpu_ram(self):
        self.thread_running = True
        self.thread = threading.Thread(target=self.collect_cpu_ram)
        self.thread.start()

    def stop_collecting_cpu_ram(self):
        if self.thread is None:
            return

        self.thread_running = False
        self.thread.join()

        df_i = pd.DataFrame(self.cpu_ram_info["idle"][-30:], columns=['timestamp', 'cpu_usage', 'used_ram'])
        df_i['status'] = 'idle'
        df_l = pd.DataFrame(self.cpu_ram_info["load"], columns=['timestamp', 'cpu_usage', 'used_ram'])
        df_l['status'] = 'load'
        df_c = pd.DataFrame(self.cpu_ram_info["cleanup"][:30], columns=['timestamp', 'cpu_usage', 'used_ram'])
        df_c['status'] = 'cleanup'
        self.clear_collection()
        return pd.concat([df_i, df_l, df_c], ignore_index=True)


def get_results(deployment_descriptor):
    max_attempts = 3
    namespace = deployment_descriptor["applications"][0]["application_namespace"]
    command = f"sudo ctr -n oakestra task exec --exec-id exec-1 test1.{namespace}.client.test.instance.0 cat results.json"

    try:
        for i in range(max_attempts):
            # Run the command
            result = subprocess.run(command, check=True, text=True, capture_output=True, shell=True)

            if result.stderr:
                print("Command error output:")
                print(result.stderr)
                exit(1)

            data: str = result.stdout
            lines = data.splitlines()
            if len(lines) > 0 and lines[-1] == "done":
                res = "\n".join(lines[:-1])
                with open("../tmp.txt", 'a') as file:
                    file.write(res)
                return res

            time.sleep(10)
        print(f"Could not retrieve the results within {max_attempts} tries.")
        exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Command '{e.cmd}' returned non-zero exit status {e.returncode}.")
        print(f"Error output: {e.stderr}")
        exit(1)

import time
import sys
import json
import requests
import random
import socket
import signal
import subprocess

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

SYSTEM_MANAGER_HOST = "0.0.0.0"
SYSTEM_MANAGER_PORT = "10000"
NET_MANAGER_PORT = "6000"
SYSTEM_MANAGER_URL = f"{SYSTEM_MANAGER_HOST}:{SYSTEM_MANAGER_PORT}"
NET_MANAGER_URL = f"{SYSTEM_MANAGER_HOST}:{NET_MANAGER_PORT}"
SLA_FILE = "test-jitter.json"
ENABLE_EBPF = False
TEST_LENGTH = 20  # in seconds

deployment_descriptor = json.load(open(SLA_FILE))


def get_random_string(length):
    # choose from all lowercase letter
    result_str = ''.join(random.choice('qwertyuiopasdfghjklzxcvbnm') for i in range(length))
    return result_str


def getlogin():
    url = "http://" + SYSTEM_MANAGER_URL + "/api/auth/login"
    credentials = {
        "username": "Admin",
        "password": "Admin"
    }
    r = requests.post(url, json=credentials)
    return r.json()["token"]


def register_app():
    token = getlogin()

    # print(deployment_descriptor)
    head = {'Authorization': "Bearer " + token}
    url = "http://" + SYSTEM_MANAGER_URL + "/api/application"
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


def undeploy_all(app_id):
    print("\t Asking Undeployment")
    token = getlogin()
    url = "http://" + SYSTEM_MANAGER_URL + "/api/application/" + str(app_id)
    resp = requests.delete(url, headers={'Authorization': 'Bearer {}'.format(token)})
    time.sleep(10)
    pass


def scale_up_service(amount, microserviceid):
    print("\t Asking scaleup of n.", amount, " insances of ", microserviceid)
    token = getlogin()
    for i in range(int(amount)):
        url = "http://" + SYSTEM_MANAGER_URL + "/api/service/" + microserviceid + "/instance"
        resp = requests.post(url, headers={'Authorization': 'Bearer {}'.format(token)})
        time.sleep(1)
    pass


def delete_all_apps():
    token = getlogin()
    url = "http://" + SYSTEM_MANAGER_URL + "/api/services"
    resp = requests.get(url, headers={'Authorization': 'Bearer {}'.format(token)})
    if resp.status_code == 200:
        json_resp = json.loads(resp.json())
        print(json_resp)
        for app in json_resp:
            url = "http://" + SYSTEM_MANAGER_URL + "/api/application/" + app.get("applicationID")
            r = requests.delete(url, headers={'Authorization': 'Bearer {}'.format(token)})
            print(r)
            print("Waiting undeployment cooldown")
            time.sleep(2)


def check_deployment(microservices):
    token = getlogin()
    head = {'Authorization': 'Bearer {}'.format(token)}
    clientip = "0.0.0.0"
    for microservice in microservices:
        url = "http://" + SYSTEM_MANAGER_URL + "/api/service/" + microservice
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


def signal_handler(sig, frame):
    print('Cleanup process started')
    delete_all_apps()
    delete_all_ebpf_modules()
    print('Cleanup completed!')
    sys.exit(0)


def delete_all_ebpf_modules():
    url = "http://" + NET_MANAGER_URL + "/ebpf"

    payload = {}
    headers = {}

    response = requests.request("DELETE", url, headers=headers, data=payload)

    if response.status_code != 200:
        return False

    return True


def enable_ebpf_proxy() -> bool:
    url = "http://" + NET_MANAGER_URL + "/ebpf"
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


def get_results():
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
            if lines[-1] == "done":
                return "\n".join(lines[:-1])

            time.sleep(10)
        print(f"Could not retrieve the results within {max_attempts} tries.")
        exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Command '{e.cmd}' returned non-zero exit status {e.returncode}.")
        print(f"Error output: {e.stderr}")
        exit(1)


def main():
    print("Test 1 - Throughput Measurement")

    print("Performing initial cleanup")
    delete_all_apps()
    delete_all_ebpf_modules()
    time.sleep(5)

    if ENABLE_EBPF:
        print("Enable ebpf proxy")
        enable_ebpf_proxy()

    print("Registration of the Application")
    appid, microservices = register_app()
    if appid == "":
        print("App registration failed")
        print("Forcing undeployment. Please wait for the cleanup to finish")
        undeploy_all(appid)
        time.sleep(20)
        print("You may now fix your infrastructure and re-try the test")
        exit(1)
    signal.signal(signal.SIGINT, signal_handler)

    scale_up_service(1, microservices[0])
    scale_up_service(1, microservices[1])
    time.sleep(15)

    print("Check deployment status")
    succeeded, returntext = check_deployment(microservices)
    attempt = 1
    while not succeeded:
        if attempt > 3:
            print("Deployment failed with error: ", returntext)
            print("Forcing undeployment. Please wait for the cleanup to finish")
            delete_all_apps()
            time.sleep(60)
            print("You may now fix your infrastructure and re-try the test")
            exit(1)
        attempt += 1
        print("Deployment not finished yet")
        time.sleep(10)
        succeeded, returntext = check_deployment(microservices)

    print("Waiting for test results.")
    time.sleep(TEST_LENGTH)
    res = get_results()
    print(res)


if __name__ == '__main__':
    main()

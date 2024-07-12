from flask import Flask, request
import time
import csv
import sys
import json
import requests
import os
import random
import socket
import signal

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

SYSTEM_MANAGER_URL = "0.0.0.0:10000"
SLA_FILE = "latency-test.json"
SERVER_ADDRESS = "10.19.1.254"

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
    print('Cleanup completed!')
    sys.exit(0)


if __name__ == '__main__':
    print("Test 1 - Latency Measurement")

    print("Performing initial cleanup")
    delete_all_apps()
    time.sleep(5)

    print("Registration of the Iperf Application")
    appid, microservices = register_app()
    if appid == "":
        print("App registration failed")
        print("Forcing undeployment. Please wait for the cleanup to finish")
        undeploy_all(appid)
        time.sleep(20)
        print("You may now fix your infrastructure and re-try the test")
        exit(1)

    scale_up_service(1, microservices[0])
    scale_up_service(1, microservices[1])

    print("Waiting for 10 seconds cooldown")
    time.sleep(10)

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
    time.sleep(10)  # wait at least 10 seconds more such that the iperf test is done for sure
    namespace = deployment_descriptor["applications"][0]["application_namespace"]
    signal.signal(signal.SIGINT, signal_handler)
    print('The test should be done by now. Use the following command to read the test results from within the client '
          'container and store them in a file called test1.json on your file system.: ')
    print('|-------------------------------------------------------------------------|')
    print('sudo ctr -n oakestra task exec --exec-id exec-1 test1.' + namespace + '.client.test.instance.0 cat '
                                                                                 'test1.json > test1.json')
    print('|-------------------------------------------------------------------------|')
    print('After recieving the test results, run the parser to transform the data (if you wish).')
    print('#When you`re done, press Ctrl+C to quit this script and undeploy the benchmark')
    signal.pause()

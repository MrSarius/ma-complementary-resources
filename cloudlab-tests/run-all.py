import time
import sys
import json
import signal
import socket

from Common import (enable_ebpf_proxy, register_app, scale_up_service, check_deployment, get_results, clean)
from Parser import parse_latency_sample, parse_jitter_sample, parse_throughput_sample

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

SYSTEM_MANAGER_HOST = "0.0.0.0"
SYSTEM_MANAGER_PORT = "10000"
NET_MANAGER_PORT = "6000"
SYSTEM_MANAGER_URL = f"{SYSTEM_MANAGER_HOST}:{SYSTEM_MANAGER_PORT}"
NET_MANAGER_URL = f"{SYSTEM_MANAGER_HOST}:{NET_MANAGER_PORT}"


def signal_handler(sig, frame):
    print("Performing cleanup")
    clean(SYSTEM_MANAGER_URL, NET_MANAGER_URL)
    sys.exit(0)


def test_jitter(enable_ebpf: bool):
    print("Jitter Test")
    deployment_descriptor = json.load(open("SLAs/test-jitter.json"))

    print("Performing cleanup")
    clean(SYSTEM_MANAGER_URL, NET_MANAGER_URL)

    if enable_ebpf:
        print("Enable ebpf proxy")
        enable_ebpf_proxy(NET_MANAGER_URL)

    print("Registration of the Application")
    appid, microservices = register_app(SYSTEM_MANAGER_URL, deployment_descriptor)
    if appid == "":
        print("App registration failed")
        clean(SYSTEM_MANAGER_URL, NET_MANAGER_URL)
        exit(1)
    signal.signal(signal.SIGINT, signal_handler)

    scale_up_service(1, microservices[0], SYSTEM_MANAGER_URL)
    scale_up_service(1, microservices[1], SYSTEM_MANAGER_URL)

    time.sleep(15)

    print("Check deployment status")
    succeeded, returntext = check_deployment(microservices, SYSTEM_MANAGER_URL)
    attempt = 1
    while not succeeded:
        if attempt > 3:
            print("Deployment failed with error: ", returntext)
            clean(SYSTEM_MANAGER_URL, NET_MANAGER_URL)
            exit(1)
        attempt += 1
        print("Deployment not finished yet")
        time.sleep(10)
        succeeded, returntext = check_deployment(microservices, SYSTEM_MANAGER_URL)

    print("Waiting for test results.")
    time.sleep(20)

    return get_results(deployment_descriptor)


def test_latency(enable_ebpf: bool):
    print("Latency Test")
    deployment_descriptor = json.load(open("SLAs/test-latency.json"))

    print("Performing cleanup")
    clean(SYSTEM_MANAGER_URL, NET_MANAGER_URL)

    if enable_ebpf:
        print("Enable ebpf proxy")
        enable_ebpf_proxy(NET_MANAGER_URL)

    print("Registration of the Application")
    appid, microservices = register_app(SYSTEM_MANAGER_URL, deployment_descriptor)
    if appid == "":
        print("App registration failed")
        clean(SYSTEM_MANAGER_URL, NET_MANAGER_URL)
        exit(1)
    signal.signal(signal.SIGINT, signal_handler)

    scale_up_service(1, microservices[0], SYSTEM_MANAGER_URL)
    scale_up_service(1, microservices[1], SYSTEM_MANAGER_URL)

    time.sleep(15)

    print("Check deployment status")
    succeeded, returntext = check_deployment(microservices, SYSTEM_MANAGER_URL)
    attempt = 1
    while not succeeded:
        if attempt > 3:
            print("Deployment failed with error: ", returntext)
            clean(SYSTEM_MANAGER_URL, NET_MANAGER_URL)
            exit(1)
        attempt += 1
        print("Deployment not finished yet")
        time.sleep(10)
        succeeded, returntext = check_deployment(microservices, SYSTEM_MANAGER_URL)

    print("Waiting for test results.")
    time.sleep(10)

    return get_results(deployment_descriptor)


def test_throughput(enable_ebpf: bool):
    print("Throughput Test")
    deployment_descriptor = json.load(open("SLAs/test-throughput.json"))

    print("Performing cleanup")
    clean(SYSTEM_MANAGER_URL, NET_MANAGER_URL)

    if enable_ebpf:
        print("Enable ebpf proxy")
        enable_ebpf_proxy(NET_MANAGER_URL)

    print("Registration of the Application")
    appid, microservices = register_app(SYSTEM_MANAGER_URL, deployment_descriptor)
    if appid == "":
        print("App registration failed")
        clean(SYSTEM_MANAGER_URL, NET_MANAGER_URL)
        exit(1)
    signal.signal(signal.SIGINT, signal_handler)

    scale_up_service(1, microservices[0], SYSTEM_MANAGER_URL)
    scale_up_service(1, microservices[1], SYSTEM_MANAGER_URL)

    time.sleep(15)

    print("Check deployment status")
    succeeded, returntext = check_deployment(microservices, SYSTEM_MANAGER_URL)
    attempt = 1
    while not succeeded:
        if attempt > 3:
            print("Deployment failed with error: ", returntext)
            clean(SYSTEM_MANAGER_URL, NET_MANAGER_URL)
            exit(1)
        attempt += 1
        print("Deployment not finished yet")
        time.sleep(10)
        succeeded, returntext = check_deployment(microservices, SYSTEM_MANAGER_URL)

    print("Waiting for test results.")
    time.sleep(20)
    return get_results(deployment_descriptor)

def save_samples_file(samples, file_name: str):
    with open(f"raw_data/{file_name}.txt", "w") as file:
        json.dump(samples, file)


def main():
    # raw_latency_samples = []
    # raw_throughput_samples = []
    # raw_jitter_samples = []
    #
    # raw_latency_samples_ebpf = []
    # raw_throughput_samples_ebpf = []
    # raw_jitter_samples_ebpf = []


    latency_samples = []
    throughput_samples = []
    jitter_samples = []

    latency_samples_ebpf = []
    throughput_samples_ebpf = []
    jitter_samples_ebpf = []

    # TODO ben continue until std deviation threshhold is reached
    # Tests with ebpf disabled
    # while len(latency_samples) < 1:
    #     raw = test_latency(enable_ebpf=False)
    #     # raw_latency_samples.append(raw)
    #     latency_samples.append(parse_latency_sample(raw))
    #
    # save_samples_file(latency_samples, "latency")
    #
    # while len(throughput_samples) < 1:
    #     raw = test_throughput(enable_ebpf=False)
    #     # raw_throughput_samples.append(raw)
    #     throughput_samples.append(parse_throughput_sample(raw))
    #
    # save_samples_file(throughput_samples, "throughput")
    #
    # while len(jitter_samples) < 1:
    #     raw = test_jitter(enable_ebpf=False)
    #     # raw_jitter_samples.append(raw)
    #     jitter_samples.append(parse_jitter_sample(raw))
    #
    # save_samples_file(jitter_samples, "jitter")

    # Tests with ebpf enabled
    while len(latency_samples_ebpf) < 1:
        raw = test_latency(enable_ebpf=True)
        # raw_latency_samples_ebpf.append(raw)
        latency_samples_ebpf.append(parse_latency_sample(raw))

    save_samples_file(latency_samples_ebpf, "latency_ebpf")

    while len(throughput_samples_ebpf) < 1:
        raw = test_throughput(enable_ebpf=True)
        # raw_throughput_samples_ebpf.append(raw)
        throughput_samples_ebpf.append(parse_throughput_sample(raw))

    save_samples_file(throughput_samples_ebpf, "throughput_ebpf")

    while len(jitter_samples_ebpf) < 1:
        raw = test_jitter(enable_ebpf=True)
        # raw_jitter_samples_ebpf.append(raw)
        jitter_samples_ebpf.append(parse_jitter_sample(raw))

    save_samples_file(jitter_samples_ebpf, "jitter_ebpf")

if __name__ == '__main__':
    main()

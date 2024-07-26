import time
import sys
import json
import signal
import socket

from Common import (enable_ebpf_proxy, register_app, scale_up_service, check_deployment, get_results, clean,
                    CpuRamCollector)
from Parser import parse_cpu_ram_samples

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

SYSTEM_MANAGER_HOST = "0.0.0.0"
SYSTEM_MANAGER_PORT = "10000"
NET_MANAGER_PORT = "6000"
SYSTEM_MANAGER_URL = f"{SYSTEM_MANAGER_HOST}:{SYSTEM_MANAGER_PORT}"
NET_MANAGER_URL = f"{SYSTEM_MANAGER_HOST}:{NET_MANAGER_PORT}"
collector = CpuRamCollector()


def signal_handler(sig, frame):
    print("Performing cleanup")
    clean(SYSTEM_MANAGER_URL, NET_MANAGER_URL)
    collector.stop_collecting_cpu_ram()
    sys.exit(0)


def test_jitter(enable_ebpf: bool):
    print("*** Jitter Test ***")
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
    print("*** Latency Test ***")
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
    time.sleep(20)

    return get_results(deployment_descriptor)


def test_throughput(enable_ebpf: bool):
    print("*** Throughput Test ***")
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


def test_ram_cpu(enable_ebpf: bool):
    print("*** RAM/CPU Test ***")
    deployment_descriptor = json.load(open("SLAs/test-ram-cpu.json"))

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

    print("Recording 15 seconds of idle")
    collector.set_collection_state("idle")
    collector.start_collecting_cpu_ram()
    time.sleep(15)

    scale_up_service(1, microservices[0], SYSTEM_MANAGER_URL)
    scale_up_service(1, microservices[1], SYSTEM_MANAGER_URL)

    print("Recording 15 seconds of high load")
    collector.set_collection_state("load")
    time.sleep(15)

    print("Check deployment status")
    succeeded, returntext = check_deployment(microservices, SYSTEM_MANAGER_URL)
    if not succeeded:
        clean(SYSTEM_MANAGER_URL, NET_MANAGER_URL)
        print("Deployment did not succeed during load phase of test.")
        exit(1)

    print("Recording 15 seconds of clean up")
    collector.set_collection_state("cleanup")
    clean(SYSTEM_MANAGER_URL, NET_MANAGER_URL)
    time.sleep(15)

    return collector.stop_collecting_cpu_ram()


def main():
    test_repetitions = 20

    latency_samples = []
    throughput_samples = []
    jitter_samples = []
    cpu_ram_samples = []

    latency_samples_ebpf = []
    throughput_samples_ebpf = []
    jitter_samples_ebpf = []
    cpu_ram_samples_ebpf = []

    # TODO ben continue until std deviation threshhold is reached
    # TODO empty lists after parsed to save memory
    # Tests with ebpf disabled
    while len(throughput_samples) < test_repetitions:
        throughput_samples.append(test_throughput(enable_ebpf=False))
    parse_throughput_samples(throughput_samples, "throughput")
    throughput_samples.clear()

    while len(latency_samples) < test_repetitions:
        latency_samples.append(test_latency(enable_ebpf=False))
    parse_latency_samples(latency_samples, "latency")
    latency_samples.clear()

    while len(jitter_samples) < test_repetitions:
        jitter_samples.append(test_jitter(enable_ebpf=False))
    parse_jitter_samples(jitter_samples, "jitter")
    jitter_samples.clear()

    # Tests with ebpf enabled
    while len(throughput_samples_ebpf) < test_repetitions:
        throughput_samples_ebpf.append(test_throughput(enable_ebpf=True))
    parse_throughput_samples(throughput_samples_ebpf, "throughput_ebpf")
    throughput_samples_ebpf.clear()

    while len(latency_samples_ebpf) < test_repetitions:
        latency_samples_ebpf.append(test_latency(enable_ebpf=True))
    parse_latency_samples(latency_samples_ebpf, "latency_ebpf")
    latency_samples_ebpf.clear()

    while len(jitter_samples_ebpf) < test_repetitions:
        jitter_samples_ebpf.append(test_jitter(enable_ebpf=True))
    parse_jitter_samples(jitter_samples_ebpf, "jitter_ebpf")
    jitter_samples_ebpf.clear()

    while len(cpu_ram_samples) < test_repetitions:
        cpu_ram_samples.append(test_ram_cpu(enable_ebpf=False))
    parse_cpu_ram_samples(cpu_ram_samples, "cpu_ram")

    while len(cpu_ram_samples_ebpf) < test_repetitions:
        cpu_ram_samples_ebpf.append(test_ram_cpu(enable_ebpf=True))
    parse_cpu_ram_samples(cpu_ram_samples_ebpf, "cpu_ram_ebpf")


if __name__ == '__main__':
    main()

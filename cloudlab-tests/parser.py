import re
import json

import pandas as pd

BASE_PATH = "raw_data"


def parse_latency_samples(samples: [], filename: str):
    if len(samples) <= 0:
        print("Error parsing latency measurement.")

    data = {}

    for i in range(len(samples)):
        rtts = re.findall(r'rtt=(\d+\.\d+) ms', samples[i])
        data[f"Measurement_{i + 1}"] = rtts[:15]
        amount = len(rtts)

    data["Ping_Nr."] = list(range(1, 16))

    df = pd.DataFrame(data)
    df.to_csv(f"{BASE_PATH}/{filename}.csv", index=False)


def parse_jitter_samples(samples: [], filename: str):
    data = {
        'Measurement': list(range(1, len(samples) + 1)),
        'Jitter': []
    }

    for sample in samples:
        parsed = json.loads(sample)
        data["Jitter"].append(parsed['end']['streams'][0]['udp']['jitter_ms'])

    df = pd.DataFrame(data)
    df.to_csv(f"{BASE_PATH}/{filename}.csv", index=False)


def parse_throughput_samples(samples: [], filename: str):
    if len(samples) <= 0:
        print("Error parsing throughput measurement.")

    amount_intervals = len(json.loads(samples[0])["intervals"])
    time = list(range(1, amount_intervals + 1))  # assuming one measurement per second!
    data = {
        'Seconds': time,
    }

    for i in range(len(samples)):
        measurement = []
        parsed = json.loads(samples[i])
        for interval in parsed.get('intervals', []):
            for stream in interval.get('streams', []):
                throughput = stream.get('bits_per_second')
                if throughput is not None:
                    measurement.append(float(throughput))
        data[f"Measurement_{i + 1}"] = measurement

    df = pd.DataFrame(data)
    df.to_csv(f"{BASE_PATH}/{filename}.csv", index=False)


def parse_cpu_ram_samples(samples: [], filename: str):
    for i in range(len(samples)):
        samples[i]['measurement'] = i
    pd.concat(samples, ignore_index=True).to_csv(f"{BASE_PATH}/{filename}.csv", index=False)


def parse_bottleneck_samples(samples: [], target_bws, filename: str):
    if len(target_bws) != len(samples):
        print("Error parsing bottleneck measurement.")
        return

    latency_regex = r"(\d+\.\d+|\d+)/(\d+\.\d+|\d+)/(\d+\.\d+|\d+)/(\d+\.\d+) ms"
    lost_total_regex = r"(\d+)/(\d+) \((\d+\.\d+|\d+)%\)"

    data = {
        'target_bandwidth': target_bws,
        'avg_latency': [],
        'min_latency': [],
        'max_latency': [],
        'loss_percentage': []
    }

    for sample in samples:
        latency_match = re.search(latency_regex, sample)
        if latency_match:
            avg_latency = float(latency_match.group(1))
            min_latency = float(latency_match.group(2))
            max_latency = float(latency_match.group(3))
            stdev_latency = float(latency_match.group(4))
        else:
            print("Error parsing bottleneck measurement.")
            return

        # Find the lost and total datagrams
        lost_total_match = re.search(lost_total_regex, sample)
        if lost_total_match:
            lost = int(lost_total_match.group(1))
            total = int(lost_total_match.group(2))
            lost_percentage = float(lost_total_match.group(3))
        else:
            print("Error parsing bottleneck measurement.")
            return

        data['avg_latency'].append(avg_latency)
        data['min_latency'].append(min_latency)
        data['max_latency'].append(max_latency)
        data['loss_percentage'].append(lost_percentage)

    df = pd.DataFrame(data)
    df.to_csv(f"{BASE_PATH}/{filename}.csv", index=False)


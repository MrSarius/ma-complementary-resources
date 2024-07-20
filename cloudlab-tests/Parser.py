import re
from typing import List
import json
import os


def parse_latency_sample(sample: str) -> List[float]:
    return re.findall(r'rtt=(\d+\.\d+) ms', sample)

def parse_jitter_sample(sample: str) -> float:
    parsed = json.loads(sample)
    return float(parsed['end']['streams'][0]['udp']['jitter_ms'])

def parse_throughput_sample(sample: str):
    parsed = json.loads(sample)

    interval_throughputs = []
    for interval in parsed.get('intervals', []):
        for stream in interval.get('streams', []):
            throughput = stream.get('bits_per_second')
            if throughput is not None:
                interval_throughputs.append(float(throughput))

    return interval_throughputs

def save_samples_file(samples, file_name: str):
    with open(f"raw_data/{file_name}.txt", "w") as file:
        json.dump(samples, file)

def load_samples_file(file_name: str) -> []:
    path = f"raw_data/{file_name}.txt"

    if not os.path.exists(path):
        return []

    with open(path, "r") as file:
        return json.load(file)
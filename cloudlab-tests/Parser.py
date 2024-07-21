import re
from typing import List
import json
import os

import pandas as pd
from CommandNotFound.db.creator import measure

BASE_PATH = "raw_data"

def parse_latency_sample(sample: str) -> List[float]:
    return re.findall(r'rtt=(\d+\.\d+) ms', sample)

def parse_jitter_sample(sample: str) -> float:
    parsed = json.loads(sample)
    return float(parsed['end']['streams'][0]['udp']['jitter_ms'])

def parse_throughput_samples(samples: [], filename: str):
    if len(samples) > 0:
        print("Error parsing throughput measurement.")

    amount_intervals = len(json.loads(samples[0])["intervals"])
    time = list(range(1, amount_intervals + 1)) # assuming one measurement per second!
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

def save_samples_file(samples, file_name: str):
    with open(f"raw_data/{file_name}.txt", "w") as file:
        json.dump(samples, file)

def load_samples_file(file_name: str) -> []:
    path = f"raw_data/{file_name}.txt"

    if not os.path.exists(path):
        return []

    with open(path, "r") as file:
        return json.load(file)
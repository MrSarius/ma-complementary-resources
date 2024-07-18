import re
from typing import List
import json
import os

latency_samples = []
throughput_samples = []
jitter_samples = []

latency_samples_ebpf = []
throughput_samples_ebpf = []
jitter_samples_ebpf = []

# def load_from_files():
#     for root, dirs, files in os.walk("raw_data"):
#         for file in files:
#             file_path = os.path.join(root, file)
#             with open(file_path, 'r') as f:
#                 if file == "jitter.txt":
#                     raw = json.load(f)
#                     global jitter_samples
#                     jitter_samples = list(map(lambda s: parse_jitter_sample(s), raw))
#                 elif file == "latency.txt":
#                     raw = json.load(f)
#                     global jitter_samples
#                     jitter_samples = list(map(lambda s: parse_jitter_sample(s), raw))
#                 elif file == "throughput.txt":
#                     raw = json.load(f)
#                     global jitter_samples
#                     jitter_samples = list(map(lambda s: parse_jitter_sample(s), raw))
#                 elif file == "jitter_ebpf.txt":
#                     raw = json.load(f)
#                     global jitter_samples
#                     jitter_samples = list(map(lambda s: parse_jitter_sample(s), raw))
#                 elif file == "latency_ebpf.txt":
#                     raw = json.load(f)
#                     global jitter_samples
#                     jitter_samples = list(map(lambda s: parse_jitter_sample(s), raw))
#                 elif file == "throughput_ebpf.txt":
#                     raw = json.load(f)
#                     global jitter_samples
#                     jitter_samples = list(map(lambda s: parse_jitter_sample(s), raw))



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

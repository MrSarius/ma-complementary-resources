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
    df = pd.read_csv(f'{BASE_PATH}/cpumemoryusage.csv')
    df['timestamp'] = df['timestamp'].astype('int')
    df['cpu_usage'] = df['cpu_usage'].str.rstrip('%').astype('float')
    df['free_ram'] = df['free_ram'].str.rstrip('KiB').astype('int')

    if len(samples) <= 0:
        print("Error parsing throughput measurement.")

    for i in range(len(samples)):
        lines = samples[i].splitlines()
        start_t = int(lines[0])
        end_t = int(lines[1])

        idle_mask = (df['timestamp'] >= start_t - 10 * 1000) & (df['timestamp'] < start_t)
        idle_df = df.loc[idle_mask, ['timestamp', 'cpu_usage', 'free_ram']]
        idle_df['status'] = 'idle'

        load_mask = (df['timestamp'] >= start_t) & (df['timestamp'] <= end_t)
        load_df = df.loc[load_mask, ['timestamp', 'cpu_usage', 'free_ram']]
        load_df['status'] = 'load'

        cleanup_mask = (df['timestamp'] > end_t) & (df['timestamp'] <= end_t + 10 * 1000)
        cleanup_df = df.loc[cleanup_mask, ['timestamp', 'cpu_usage', 'free_ram']]
        cleanup_df['status'] = 'cleanup'

        df = pd.concat([idle_df, load_df, cleanup_df], ignore_index=True)
        df['measurement'] = i



    # df = pd.DataFrame(data)
    # df.to_csv(f"{BASE_PATH}/{filename}.csv", index=False)
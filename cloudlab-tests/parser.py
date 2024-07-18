# import json
#
# # Load the JSON data from the file
# with open('test1.json', 'r') as file:
#     data = json.load(file)
#
# # Extract the jitter value from the end summary
# jitter = data['end']['streams'][0]['udp']['jitter_ms']
#
# # Extract the latency values from the intervals (correcting the interpretation)
# latencies = [interval['sum']['seconds'] for interval in data['intervals']]
#
# # Save the extracted values to a .dat file
# with open('latency_jitter_data.dat', 'w') as file:
#     # Write header
#     file.write("Time Jitter Latency\n")
#     # Write data points
#     for i, latency in enumerate(latencies, start=1):
#         file.write(f"{i} {jitter} {latency}\n")
#
# print("Data successfully saved to latency_jitter_data.dat")

import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta


def plot_latency_timeseries(json_objects):
    # Parse JSON objects and extract relevant data
    data = []
    for obj in json_objects:
        result = json.loads(obj)
        start_time = datetime.strptime(result['start']['timestamp']['time'], '%Y-%m-%dT%H:%M:%S.%fZ')
        intervals = result['intervals']
        for interval in intervals:
            timestamp = start_time + timedelta(seconds=interval['sum']['start'])
            latency = interval['sum']['latency_ms']
            data.append({'timestamp': timestamp, 'latency': latency})

    # Convert data to DataFrame
    df = pd.DataFrame(data)

    # Group by timestamp and calculate mean and standard deviation of latency
    df_grouped = df.groupby('timestamp').agg(
        latency_mean=pd.NamedAgg(column='latency', aggfunc='mean'),
        latency_std=pd.NamedAgg(column='latency', aggfunc='std')
    ).reset_index()

    # Plotting
    plt.figure(figsize=(14, 7))
    sns.lineplot(x='timestamp', y='latency_mean', data=df_grouped, label='Mean Latency')
    plt.fill_between(
        df_grouped['timestamp'],
        df_grouped['latency_mean'] - df_grouped['latency_std'],
        df_grouped['latency_mean'] + df_grouped['latency_std'],
        color='blue', alpha=0.2, label='Standard Deviation'
    )
    plt.xlabel('Time')
    plt.ylabel('Latency (ms)')
    plt.title('Latency Time Series with Error Bands')
    plt.legend()
    plt.show()
import json

# Load the JSON data from the file
with open('test1.json', 'r') as file:
    data = json.load(file)

# Extract the jitter value from the end summary
jitter = data['end']['streams'][0]['udp']['jitter_ms']

# Extract the latency values from the intervals (correcting the interpretation)
latencies = [interval['sum']['seconds'] for interval in data['intervals']]

# Save the extracted values to a .dat file
with open('latency_jitter_data.dat', 'w') as file:
    # Write header
    file.write("Time Jitter Latency\n")
    # Write data points
    for i, latency in enumerate(latencies, start=1):
        file.write(f"{i} {jitter} {latency}\n")

print("Data successfully saved to latency_jitter_data.dat")
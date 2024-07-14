if [ -z "$TARGET_IP" ]; then
  echo "TARGET_IP environment variable is not set."
  exit 1
fi

# Throughput test using iperf3 over TCP
echo "Running TCP throughput test..."
iperf3 -c 10.30.0.1 -u -b 0 -t 10 -J > throughput.json

# Jitter test using iperf3 over UDP
echo "Running UDP jitter test..."
iperf3 -c $TARGET_IP -u -b 10M -t 10 > jitter.json

# Latency test using hping3 with TCP SYN packets
echo "Running TCP SYN latency test..."
hping3 -S -p 80 -c 5 -i 1 $TARGET_IP > latency.json
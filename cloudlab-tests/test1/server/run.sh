python3 simple_udp_server.py &

echo "Running TCP throughput test..."
iperf3 -s -B 0.0.0.0 -V -i 1
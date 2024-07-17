if [ -z "$TARGET_IP" ]; then
  echo "TARGET_IP environment variable is not set."
  exit 1
fi

if [ -z "$ITERATIONS" ]; then
  echo "ITERATIONS environment variable is not set."
  exit 1
fi

for (( i=1; i<=$ITERATIONS; i++ ))
do
  echo "Iteration $i"

  echo "Running TCP throughput test..."
  iperf3 -c $TARGET_IP -b 0 -t 10 -J > throughput_$i.json

  echo "Running UDP jitter test..."
  iperf3 -c $TARGET_IP -u -b 1M -t 10 -J > jitter_$i.json

  echo "Running TCP SYN latency test..."
  hping3 -2 $TARGET_IP -p 12345 -d 120
done

echo "Done! You may collect the results now and shut down the deployment."
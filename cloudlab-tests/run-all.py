import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'jitter'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'latency'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'throughput'))

from jitter.TestJitter import test_jitter
from latency.TestLatency import test_latency
from throughput.TestThroughput import test_throughput

jitter = test_jitter()
latency = test_latency()
throughput = test_throughput()

print("")

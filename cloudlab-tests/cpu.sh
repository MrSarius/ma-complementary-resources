#!/bin/bash

echo "timestamp,cpu_usage,free_ram" > raw_data/cpumemoryusage.csv

#numer of attempt
max=10000000
#number of seconds between one attempt and another
sleep=0.5

for _ in $(seq 1 $max)
do
    cpu=$(awk '{u=$2+$4; t=$2+$4+$5; if (NR==1){u1=u; t1=t;} else print ($2+$4-u1) * 100 / (t-t1) "%"; }' <(grep 'cpu ' /proc/stat) <(sleep 1;grep 'cpu ' /proc/stat))
    mem=$(free | grep Mem | awk '{print $3}')
    echo "$(($(date +%s%N)/1000000)),$cpu,${mem}KiB" >> raw_data/cpumemoryusage.csv
    sleep $sleep
done
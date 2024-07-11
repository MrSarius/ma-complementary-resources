sudo ip netns exec ns1 tcpdump -i veth-ns1-peer
sudo ip netns exec ns2 tcpdump -i veth-ns2-peer
sudo tcpdump -i br0
sudo cat /sys/kernel/debug/tracing/trace_pipe
sudo ip netns exec ns1 ping -c 1 216.58.206.35
sudo bpftool map dump name fw_rules

Demo notes
Show drawing on iPad
Show eBPF. Why TC and not XDP? Why no chaining? Show the coole compilation process 
-> go generate
sudo ./script.sh
-> Network flows
sudo ./ebpfManager
-> Attaches firewall, thus everything (TCP, UDP and ICMO gets blocked)
Enable traffic via Postman
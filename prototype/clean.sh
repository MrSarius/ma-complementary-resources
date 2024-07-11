#!/bin/bash

# Names of the network namespaces
NS1="ns1"
NS2="ns2"

# Name of the bridge
BRIDGE="br0"

# Delete the veth pairs (automatically deletes the peer devices)
ip link del veth-$NS1
ip link del veth-$NS2

# Remove the bridge
ip link del name $BRIDGE type bridge

# Remove the network namespaces
ip netns del $NS1
ip netns del $NS2

# Clean up NAT rules set by iptables
iptables -t nat -D POSTROUTING -s 10.0.0.0/24 -o eth0 -j MASQUERADE

echo "Cleanup complete. Network namespaces, bridge, and veth pairs removed."

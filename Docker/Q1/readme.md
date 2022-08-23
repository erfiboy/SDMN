# Routing without router

### Solution one (bridge ip)
When there is not a router we should route packets through root namespace. So we assign br1 and br2 ip addresses, and root namespace can see and have a link to the namespaces with the corresponding bridges. And then we should route packets in the root namespace to do so we should write 1 to proc/sys/net/ipv4/ip_forward.

 >On a Linux system, IP forwarding is enabled when the file /proc/sys/net/ipv4/ip_forward contains a 1 and disabled when it contains a 0. The command echo writes the given argument, the string "1", to the standard output. Using the redirect operator (>) and a filename, the output of the command is written to a file.

 so we should create the bridges with following command:
 ```bash
ip link add <bridge_name> type bridge
ip link set dev <bridge_name> up
ip addr add 172.0.0.1/24 dev <bridge_name> 
 ```
then we should set a default route in each node:
```bash
ip netns exec <node_name> route add -net 0.0.0.0/0 gw <connected bridge ip>
```
and enable IP forwarding in linux:
```bash
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward
```

so that the nodes in the namespaces could ping each other, the following is the result:
```bash
erfan@erfiboy:/opt/HW2/HW2-sdmn/Q1$ ip netns exec node4 ping 172.0.0.2
PING 172.0.0.2 (172.0.0.2) 56(84) bytes of data.
64 bytes from 172.0.0.2: icmp_seq=1 ttl=64 time=0.058 ms
64 bytes from 172.0.0.2: icmp_seq=2 ttl=64 time=0.056 ms
64 bytes from 172.0.0.2: icmp_seq=3 ttl=64 time=0.055 ms
64 bytes from 172.0.0.2: icmp_seq=4 ttl=64 time=0.054 ms
64 bytes from 172.0.0.2: icmp_seq=5 ttl=64 time=0.056 ms
64 bytes from 172.0.0.2: icmp_seq=6 ttl=64 time=0.052 ms
```

### Solution two (without bridge ip)
In this solution we add six route which route packets through root from one namespace to another. This rules will sends packet with different subnets to the connected bridge: 
```bash
ip netns exec node1 ip route add 10.10.0.0/24 dev eth-node1
ip netns exec node2 ip route add 10.10.0.0/24 dev eth-node2
ip netns exec node3 ip route add 172.0.0.0/24 dev eth-node3
ip netns exec node4 ip route add 172.0.0.0/24 dev eth-node4
```
and we should add this routes to the root namespace to send packets for each subnet to its bridge:
```bash
ip route add 10.0.0.0/24 dev br1
ip route add 172.0.0.0/24 dev br0
```
This two rules will route packet to the bridges of the corresponding subnets in the root namespace.

# Routing between VMs
When the subnets are not in the same VMs we should route the packets through the eth0 (the first Ethernet interface which is the default interface to access out side the VM).
so the routes in the subnets are the same :
```bash
ip netns exec node1 ip route add 10.10.0.0/24 dev eth-node1
ip netns exec node2 ip route add 10.10.0.0/24 dev eth-node2
ip netns exec node3 ip route add 172.0.0.0/24 dev eth-node3
ip netns exec node4 ip route add 172.0.0.0/24 dev eth-node4
```

But now we should route packet for the subnets in other vm to eth0 and we should add these routes in VMs:
```bash
ip route add 10.0.0.0/24 dev eth0
ip route add 172.0.0.0/24 dev br0
```
and rules for the second VM is as follows:

```bash
ip route add 10.0.0.0/24 dev br1
ip route add 172.0.0.0/24 dev eth0
```
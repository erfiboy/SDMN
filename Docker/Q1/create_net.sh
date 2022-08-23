#!/bin/sh
# create a namespace:       ip netns add <ns>
# delete a namespace:       ip netns del <ns>
# list of namespaces:       ip netns
# create a veth:            ip link add <name> type veth peer name <name>
# connect veth end:         ip link set <link's end name> netns <ns>
# execute a command in ns:  ip netns exec <ns> <command>
# up a link:                ip link set <link's end name> up 
#                           ip netns exec <ns> ip link set dev <link's end name> up               
# set an ip address:        ip netns exec <ns> ip address add <ip/mask> dev <link's end name>
# show route:               ip netns exec <ns> ip route 
# default gateway:          ip netns exec <ns> ip route add <ip/mask> via <ip/mask>

# create switch:   ovs-vsctl add-br <switch name>
# show the switch: ovs-vsctl show
# connect link:    ovs-vsctl add-port <switch name> <link's end name>

# cleaning work space
ip -all netns delete
ovs-vsctl del-br br0
ovs-vsctl del-br br1

# create first node 
ip netns add node1
ip link add eth-node1 type veth peer name br-node1
ip link set eth-node1 netns node1
ip netns exec node1 ip link set dev lo up  

ip netns exec node1 ip link set dev eth-node1 up  
ip netns exec node1 ip address add 172.0.0.2/24 dev eth-node1 
ip netns exec node1 ip route add 10.10.0.0/24 via 172.0.0.1

# create second node 
ip netns add node2
ip link add eth-node2 type veth peer name br-node2
ip link set eth-node2 netns node2
ip netns exec node2 ip link set dev lo up

ip netns exec node2 ip link set dev eth-node2 up  
ip netns exec node2 ip address add 172.0.0.3/24 dev eth-node2 
ip netns exec node2 ip route add 10.10.0.0/24 via 172.0.0.1

# create third node 
ip netns add node3
ip link add eth-node3 type veth peer name br-node3
ip link set eth-node3 netns node3
ip netns exec node3 ip link set dev lo up  

ip netns exec node3 ip link set dev eth-node3 up  
ip netns exec node3 ip address add 10.10.0.2/24 dev eth-node3 
ip netns exec node3 ip route add 172.0.0.0/24 via 10.10.0.1

# create fourth node 
ip netns add node4
ip link add eth-node4 type veth peer name br-node4
ip link set eth-node4 netns node4
ip netns exec node4 ip link set dev lo up  

ip netns exec node4 ip link set dev eth-node4 up  
ip netns exec node4 ip address add 10.10.0.3/24 dev eth-node4 
ip netns exec node4 ip route add 172.0.0.0/24 via 10.10.0.1

# create router 
ip netns add router
ip link add eth-router0 type veth peer name br-0
ip link add eth-router1 type veth peer name br-1

ip link set eth-router0 netns router
ip link set eth-router1 netns router
ip netns exec router ip link set dev lo up 

ip netns exec router ip link set dev eth-router1 up  
ip netns exec router ip address add 10.10.0.1/24 dev eth-router1

ip netns exec router ip link set dev eth-router0 up
ip netns exec router ip address add 172.0.0.1/24 dev eth-router0


# create switch br0
ovs-vsctl add-br br0
ovs-vsctl add-port br0 br-node1
ovs-vsctl add-port br0 br-node2
ovs-vsctl add-port br0 br-0

ip link set br-node1 up
ip link set br-node2 up
ip link set br-0 up

# create switch br1
ovs-vsctl add-br br1
ovs-vsctl add-port br1 br-node3
ovs-vsctl add-port br1 br-node4
ovs-vsctl add-port br1 br-1

ip link set br-node3 up
ip link set br-node4 up
ip link set br-1 up
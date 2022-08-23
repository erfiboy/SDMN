#!/bin/bash  

second_node_ip=$(ip netns exec $2 hostname -I | cut -f1 -d" ")

ip netns exec $1 ping $second_node_ip


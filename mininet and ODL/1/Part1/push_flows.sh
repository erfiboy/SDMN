ovs-ofctl add-flow s1 priority=500,in_port=1,actions=output:2
ovs-ofctl add-flow s1 priority=500,in_port=2,actions=output:1
ovs-ofctl add-flow s2 priority=500,in_port=1,actions=output:2
ovs-ofctl add-flow s2 priority=500,in_port=2,actions=output:1
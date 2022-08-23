ovs-ofctl add-flow r1 arp,idle_timeout=180,priority=500,actions=flood

ovs-ofctl add-flow r1 priority=500,dl_type=0x0800,nw_dst=10.0.2.0/24,actions=dec_ttl,output:2
ovs-ofctl add-flow r1 priority=500,dl_type=0x0800,nw_dst=10.0.1.0/24,actions=dec_ttl,output:1

ovs-ofctl add-flow s1 priority=500,in_port=1,actions=output:2
ovs-ofctl add-flow s1 priority=500,in_port=2,actions=output:1

ovs-ofctl add-flow s2 priority=500,in_port=1,actions=output:2
ovs-ofctl add-flow s2 priority=500,in_port=2,actions=output:1
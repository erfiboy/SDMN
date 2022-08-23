ovs-ofctl add-flow s1 "table=0,in_port=1,actions=set_field:100->tun_id,resubmit(,1)"
ovs-ofctl add-flow s1 "table=0,in_port=2,actions=set_field:200->tun_id,resubmit(,1)"
ovs-ofctl add-flow s1 "table=0,actions=resubmit(,1)"

#input
# h1
ovs-ofctl add-flow s1 table=1,tun_id=100,dl_dst=00:00:00:00:00:01,actions=output:1
ovs-ofctl add-flow s1 table=1,tun_id=100,arp,nw_dst=10.0.0.1,actions=output:1

# h2
ovs-ofctl add-flow s1 table=1,tun_id=200,dl_dst=00:00:00:00:00:01,actions=output:2
ovs-ofctl add-flow s1 table=1,tun_id=200,arp,nw_dst=10.0.0.1,actions=output:2

#output
# h1
ovs-ofctl add-flow s1 table=1,tun_id=100,dl_dst=00:00:00:00:00:02,actions=output:3
ovs-ofctl add-flow s1 table=1,tun_id=100,arp,nw_dst=10.0.0.2,actions=output:3

# h2
ovs-ofctl add-flow s1 table=1,tun_id=200,dl_dst=00:00:00:00:00:02,actions=output:3
ovs-ofctl add-flow s1 table=1,tun_id=200,arp,nw_dst=10.0.0.2,actions=output:3

ovs-ofctl add-flow s1 table=1,priority=50,actions=drop
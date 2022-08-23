 # s1
ovs-ofctl add-flow s1 "table=0,in_port=1,arp,nw_dst=10.0.0.2,actions=push_mpls:0x8847,set_field:12->mpls_label,set_field:0->mpls_tc,output:2"
ovs-ofctl add-flow s1 "table=0,in_port=1,ip,dl_type=0x0800,dl_dst=00:00:00:00:00:02,actions=push_mpls:0x8847,set_field:12->mpls_label,set_field:1->mpls_tc,output=2"

ovs-ofctl add-flow s1 "table=0,in_port=1,arp,nw_dst=10.0.0.3,actions=push_mpls:0x8847,set_field:13->mpls_label,set_field:0->mpls_tc,output:2"
ovs-ofctl add-flow s1 "table=0,in_port=1,ip,dl_type=0x0800,dl_dst=00:00:00:00:00:03,actions=push_mpls:0x8847,set_field:13->mpls_label,set_field:1->mpls_tc,output=2"

ovs-ofctl add-flow s1 in_port=2,dl_type=0x8847,mpls_tc=0,mpls_label=21,actions=pop_mpls:0x0806,output:1
ovs-ofctl add-flow s1 in_port=2,dl_type=0x8847,mpls_tc=1,mpls_label=21,actions=pop_mpls:0x0800,output:1

ovs-ofctl add-flow s1 in_port=2,dl_type=0x8847,mpls_tc=0,mpls_label=31,actions=pop_mpls:0x0806,output:1
ovs-ofctl add-flow s1 in_port=2,dl_type=0x8847,mpls_tc=1,mpls_label=31,actions=pop_mpls:0x0800,output:1

# s2
ovs-ofctl add-flow s2 "table=0,in_port=1,arp,nw_dst=10.0.0.1/32,actions=push_mpls:0x8847,set_field:21->mpls_label,set_field:0->mpls_tc,output=2"
ovs-ofctl add-flow s2 "table=0,in_port=1,ip,dl_type=0x0800,dl_dst=00:00:00:00:00:01,actions=push_mpls:0x8847,set_field:21->mpls_label,set_field:1->mpls_tc,output=2"

ovs-ofctl add-flow s2 "table=0,in_port=1,arp,nw_dst=10.0.0.3/32,actions=push_mpls:0x8847,set_field:23->mpls_label,set_field:0->mpls_tc,output=3"
ovs-ofctl add-flow s2 "table=0,in_port=1,ip,dl_type=0x0800,dl_dst=00:00:00:00:00:03,actions=push_mpls:0x8847,set_field:23->mpls_label,set_field:1->mpls_tc,output=3"

ovs-ofctl add-flow s2 "table=0,in_port=2,dl_type=0x8847,mpls_label=13,actions=output=3"
ovs-ofctl add-flow s2 "table=0,in_port=3,dl_type=0x8847,mpls_label=31,actions=output=2"

ovs-ofctl add-flow s2 in_port=2,dl_type=0x8847,mpls_tc=0,mpls_label=12,actions=pop_mpls:0x0806,output:1
ovs-ofctl add-flow s2 in_port=2,dl_type=0x8847,mpls_tc=1,mpls_label=12,actions=pop_mpls:0x0800,output:1

ovs-ofctl add-flow s2 in_port=3,dl_type=0x8847,mpls_tc=0,mpls_label=32,actions=pop_mpls:0x0806,output:1
ovs-ofctl add-flow s2 in_port=3,dl_type=0x8847,mpls_tc=1,mpls_label=32,actions=pop_mpls:0x0800,output:1

# s3 
ovs-ofctl add-flow s3 "table=0,in_port=1,arp,nw_dst=10.0.0.1,actions=push_mpls:0x8847,set_field:31->mpls_label,set_field:0->mpls_tc,output:2"
ovs-ofctl add-flow s3 "table=0,in_port=1,ip,dl_type=0x0800,dl_dst=00:00:00:00:00:01,actions=push_mpls:0x8847,set_field:31->mpls_label,set_field:1->mpls_tc,output=2"

ovs-ofctl add-flow s3 "table=0,in_port=1,arp,nw_dst=10.0.0.2,actions=push_mpls:0x8847,set_field:32->mpls_label,set_field:0->mpls_tc,output:2"
ovs-ofctl add-flow s3 "table=0,in_port=1,ip,dl_type=0x0800,dl_dst=00:00:00:00:00:02,actions=push_mpls:0x8847,set_field:32->mpls_label,set_field:1->mpls_tc,output=2"

ovs-ofctl add-flow s3 in_port=2,dl_type=0x8847,mpls_tc=0,mpls_label=13,actions=pop_mpls:0x0806,output:1
ovs-ofctl add-flow s3 in_port=2,dl_type=0x8847,mpls_tc=1,mpls_label=13,actions=pop_mpls:0x0800,output:1

ovs-ofctl add-flow s3 in_port=2,dl_type=0x8847,mpls_tc=0,mpls_label=23,actions=pop_mpls:0x0806,output:1
ovs-ofctl add-flow s3 in_port=2,dl_type=0x8847,mpls_tc=1,mpls_label=23,actions=pop_mpls:0x0800,output:1
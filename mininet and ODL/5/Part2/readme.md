## Connect VMs 
#### VM1
```bash
sh ovs-vsctl add-port s1 vtep -- set interface vtep type=vxlan option:key=flow ofport_request=3 option:remote_ip=192.168.43.88
```
#### VM2
```bash
sh ovs-vsctl add-port s1 vtep -- set interface vtep type=vxlan option:key=flow ofport_request=3 option:remote_ip=192.168.43.191
```

## Result
### result VM1
```bash
mininet> blue1 ping -c 10 10.0.0.2
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=99.8 ms
64 bytes from 10.0.0.2: icmp_seq=2 ttl=64 time=18.9 ms
64 bytes from 10.0.0.2: icmp_seq=3 ttl=64 time=41.1 ms
64 bytes from 10.0.0.2: icmp_seq=4 ttl=64 time=63.6 ms
64 bytes from 10.0.0.2: icmp_seq=5 ttl=64 time=284 ms
64 bytes from 10.0.0.2: icmp_seq=6 ttl=64 time=77.5 ms
64 bytes from 10.0.0.2: icmp_seq=7 ttl=64 time=337 ms
64 bytes from 10.0.0.2: icmp_seq=8 ttl=64 time=323 ms
64 bytes from 10.0.0.2: icmp_seq=9 ttl=64 time=73.5 ms
64 bytes from 10.0.0.2: icmp_seq=10 ttl=64 time=9.08 ms

--- 10.0.0.2 ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9014ms
rtt min/avg/max/mdev = 9.075/132.787/337.474/122.514 ms 
mininet> green1 ping -c 10 10.0.0.2
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=193 ms
64 bytes from 10.0.0.2: icmp_seq=2 ttl=64 time=312 ms
64 bytes from 10.0.0.2: icmp_seq=3 ttl=64 time=334 ms
64 bytes from 10.0.0.2: icmp_seq=4 ttl=64 time=59.8 ms
64 bytes from 10.0.0.2: icmp_seq=5 ttl=64 time=382 ms
64 bytes from 10.0.0.2: icmp_seq=6 ttl=64 time=10.9 ms
64 bytes from 10.0.0.2: icmp_seq=7 ttl=64 time=17.1 ms
64 bytes from 10.0.0.2: icmp_seq=8 ttl=64 time=44.4 ms
64 bytes from 10.0.0.2: icmp_seq=9 ttl=64 time=267 ms
64 bytes from 10.0.0.2: icmp_seq=10 ttl=64 time=197 ms

--- 10.0.0.2 ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9008ms
rtt min/avg/max/mdev = 10.892/181.742/381.583/133.372 ms
mininet> 
```

### result VM2

```bash
mininet> green2 ping -c 10 10.0.0.1
PING 10.0.0.1 (10.0.0.1) 56(84) bytes of data.
64 bytes from 10.0.0.1: icmp_seq=1 ttl=64 time=273 ms
64 bytes from 10.0.0.1: icmp_seq=2 ttl=64 time=99.9 ms
64 bytes from 10.0.0.1: icmp_seq=3 ttl=64 time=16.5 ms
64 bytes from 10.0.0.1: icmp_seq=4 ttl=64 time=40.9 ms
64 bytes from 10.0.0.1: icmp_seq=5 ttl=64 time=61.2 ms
64 bytes from 10.0.0.1: icmp_seq=6 ttl=64 time=82.1 ms
64 bytes from 10.0.0.1: icmp_seq=7 ttl=64 time=205 ms
64 bytes from 10.0.0.1: icmp_seq=8 ttl=64 time=24.8 ms
64 bytes from 10.0.0.1: icmp_seq=9 ttl=64 time=51.5 ms
64 bytes from 10.0.0.1: icmp_seq=10 ttl=64 time=173 ms

--- 10.0.0.1 ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9012ms
rtt min/avg/max/mdev = 16.511/102.789/273.081/81.562 ms
mininet> blue2 ping -c 4 10.0.0.1
PING  10.0.0.1 ( 10.0.0.1) 56(84) bytes of data.
64 bytes from  10.0.0.1: icmp_seq=1 ttl=64 time=307 ms
64 bytes from  10.0.0.1: icmp_seq=2 ttl=64 time=256 ms
64 bytes from  10.0.0.1: icmp_seq=3 ttl=64 time=280 ms
64 bytes from  10.0.0.1: icmp_seq=4 ttl=64 time=102 ms
64 bytes from  10.0.0.1: icmp_seq=5 ttl=64 time=326 ms
64 bytes from  10.0.0.1: icmp_seq=6 ttl=64 time=42.5 ms
64 bytes from  10.0.0.1: icmp_seq=7 ttl=64 time=68.7 ms
64 bytes from  10.0.0.1: icmp_seq=8 ttl=64 time=193 ms
64 bytes from  10.0.0.1: icmp_seq=9 ttl=64 time=209 ms
64 bytes from  10.0.0.1: icmp_seq=10 ttl=64 time=232 ms

--- 10.0.0.1 ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9012ms
rtt min/avg/max/mdev = 42.499/201.536/325.768/94.613 ms
mininet> 

```

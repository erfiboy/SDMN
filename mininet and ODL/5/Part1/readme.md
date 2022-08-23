### Connect two vms 
Run this script in both vms don't forget to change ip :)
```bash
sh ovs-vsctl add-port s1 vtep -- set interface vtep type=vxlan option:key=flow ofport_request=3 option:remote_ip=192.168.31.57
```
### result VM1
```bash
mininet> blue1 ping -c 4 10.0.0.2
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=50.1 ms
64 bytes from 10.0.0.2: icmp_seq=2 ttl=64 time=69.5 ms
64 bytes from 10.0.0.2: icmp_seq=3 ttl=64 time=91.6 ms
64 bytes from 10.0.0.2: icmp_seq=4 ttl=64 time=215 ms

--- 10.0.0.2 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3005ms
rtt min/avg/max/mdev = 50.110/106.429/214.551/64.123 ms
mininet> green1 ping -c 4 10.0.0.2
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=33.0 ms
64 bytes from 10.0.0.2: icmp_seq=2 ttl=64 time=55.8 ms
64 bytes from 10.0.0.2: icmp_seq=3 ttl=64 time=77.4 ms
64 bytes from 10.0.0.2: icmp_seq=4 ttl=64 time=99.6 ms

--- 10.0.0.2 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3005ms
rtt min/avg/max/mdev = 32.982/66.440/99.558/24.738 ms
mininet> 
```

### result VM2

```bash
mininet> green2 ping -c 4 10.0.0.1
PING 10.0.0.1 (10.0.0.1) 56(84) bytes of data.
64 bytes from 10.0.0.1: icmp_seq=1 ttl=64 time=29.3 ms
64 bytes from 10.0.0.1: icmp_seq=2 ttl=64 time=7.60 ms
64 bytes from 10.0.0.1: icmp_seq=3 ttl=64 time=73.3 ms
64 bytes from 10.0.0.1: icmp_seq=4 ttl=64 time=94.3 ms

--- 10.0.0.1 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3005ms
rtt min/avg/max/mdev = 7.598/51.131/94.316/34.388 ms
mininet> blue2 ping -c 4 10.0.0.1
PING 10.0.0.1 (10.0.0.1) 56(84) bytes of data.
64 bytes from 10.0.0.1: icmp_seq=1 ttl=64 time=6.64 ms
64 bytes from 10.0.0.1: icmp_seq=2 ttl=64 time=27.3 ms
64 bytes from 10.0.0.1: icmp_seq=3 ttl=64 time=49.9 ms
64 bytes from 10.0.0.1: icmp_seq=4 ttl=64 time=73.1 ms

--- 10.0.0.1 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3005ms
rtt min/avg/max/mdev = 6.635/39.247/73.103/24.829 ms
mininet> 

```

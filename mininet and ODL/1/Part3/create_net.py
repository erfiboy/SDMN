from mininet.net import Mininet
from mininet.node import OVSKernelSwitch
from mininet.cli import CLI
from mininet.link import TCLink

def topology():
    net = Mininet(
        controller=None,
        switch=OVSKernelSwitch ,
        link=TCLink
        )

    # Adding hosts
    h1 = net.addHost(
    name="H1",
    ip="10.0.0.1/24",
    mac="00:00:00:00:00:01",
    defaultRoute = "via 10.0.0.1"
    )

    h2 = net.addHost(
    name="H2",
    ip="10.0.0.2/24",
    mac="00:00:00:00:00:02",
    defaultRoute = "via 10.0.0.2"
    )

    h3 = net.addHost(
    name="H3",
    ip="10.0.0.3/24",
    mac="00:00:00:00:00:03",
    defaultRoute = "via 10.0.0.3"
    )

    s1 = net.addSwitch(
        name = "s1"
    )

    s2 = net.addSwitch(
        name = "s2"
    )

    
    s3 = net.addSwitch(
        name = "s3"
    )

    net.addLink(h1,s1)   
    net.addLink(h2,s2)
    net.addLink(h3,s3) 
    net.addLink(s1,s2)
    net.addLink(s2,s3)

    net.build()
    net.start()
    CLI(net)
    net.stop()


if __name__ == '__main__':
    topology()
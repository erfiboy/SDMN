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
    ip="10.0.1.1/24",
    mac="00:00:00:00:00:01",
    defaultRoute = "via 10.0.1.1"
    )

    h2 = net.addHost(
    name="H2",
    ip="10.0.2.1/24",
    mac="00:00:00:00:00:02",
    defaultRoute = "via 10.0.2.1"
    )

    s1 = net.addSwitch(
        name = "s1"
    )

    s2 = net.addSwitch(
        name = "s2"
    )

    r1 = net.addSwitch(
        name = "r1"
    )

    net.addLink(h1,s1)    
    net.addLink(h2,s2)
    net.addLink(s1,r1)
    net.addLink(s2,r1)

    net.build()
    net.start()
    CLI(net)
    net.stop()


if __name__ == '__main__':
    topology()
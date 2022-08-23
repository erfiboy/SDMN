from mininet.net import Mininet
from mininet.node import RemoteController , OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
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
    )

    h2 = net.addHost(
    name="H2",
    ip="10.0.0.2/24",
    )

    s1 = net.addSwitch(
        name = "s1"
    )

    s2 = net.addSwitch(
        name = "s2"
    )

    net.addLink(h1,s1)
    net.addLink(s1,s2)
    net.addLink(s2,h2)

    net.build()
    net.start()
    CLI(net)
    net.stop()


if __name__ == '__main__':
    topology()
from mininet.net import Mininet
from mininet.node import RemoteController , OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink

def topology():
    net = Mininet(
        controller=RemoteController,
        switch=OVSKernelSwitch,
        link=TCLink
        )

    # Adding hosts
    h1 = net.addHost(
    name="H1",
    ip="10.0.0.1/24",
    mac="00:00:00:00:00:00"
    )

    h2 = net.addHost(
    name="H2",
    ip="10.0.0.2/24",
    mac="00:00:00:00:00:01"
    )

    h3 = net.addHost(
    name="H3",
    ip="10.0.0.3/24",
    mac="00:00:00:00:00:02"
    )

    h4 = net.addHost(
    name="H4",
    ip="10.0.0.4/24",
    mac="00:00:00:00:00:03"
    )

    h5 = net.addHost(
    name="H5",
    ip="10.0.0.5/24",
    mac="00:00:00:00:00:04"
    )

    h6 = net.addHost(
    name="H6",
    ip="10.0.0.6/24",
    mac="00:00:00:00:00:05"
    )

    h7 = net.addHost(
    name="H7",
    ip="10.0.0.7/24",
    mac="00:00:00:00:00:06"
    )

    h8 = net.addHost(
    name="H8",
    ip="10.0.0.8/24",
    mac="00:00:00:00:00:07",
    )

    s1 = net.addSwitch(
        name = "s1",
        protocols= "OpenFlow13"
    )

    s2 = net.addSwitch(
        name = "s2",
        protocols= "OpenFlow13"
    )

    s3 = net.addSwitch(
        name = "s3",
        protocols= "OpenFlow13"
    )

    s4 = net.addSwitch(
        name = "s4",
        protocols= "OpenFlow13"
    )

    s5 = net.addSwitch(
        name = "s5",
        protocols= "OpenFlow13"
    )

    s6 = net.addSwitch(
        name = "s6",
        protocols= "OpenFlow13"
    )

    s7 = net.addSwitch(
        name = "s7",
        protocols= "OpenFlow13"
    )

    net.addLink(h1,s1)
    net.addLink(h2,s1)
    net.addLink(h3,s2)
    net.addLink(h4,s2)
    net.addLink(h5,s3)
    net.addLink(h6,s3)
    net.addLink(h7,s4)
    net.addLink(h8,s4)
    net.addLink(s1,s5)
    net.addLink(s2,s5)
    net.addLink(s3,s6)
    net.addLink(s4,s6)
    net.addLink(s5,s7)
    net.addLink(s6,s7)

    c1 = net.addController(name="c1", ip="127.0.0.1", port=6633)

    s1.start([c1])
    s2.start([c1])
    s3.start([c1])
    s4.start([c1])
    s5.start([c1])
    s6.start([c1])
    s7.start([c1])

    net.build()
    net.start()
    CLI(net)
    net.stop()


if __name__ == '__main__':
    topology()
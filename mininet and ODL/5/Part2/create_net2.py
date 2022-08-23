from mininet.net import Mininet
from mininet.node import RemoteController , OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink

def topology():
    net = Mininet(
        controller=RemoteController,
        switch=OVSKernelSwitch ,
        link=TCLink
        )

    # Adding hosts

    h1 = net.addHost(
    name="green1",
    ip="10.0.0.1/24",
    mac="00:00:00:00:00:01",
    )

    h2 = net.addHost(
    name="blue1",
    ip="10.0.0.1/24",
    mac="00:00:00:00:00:01",
    )

    s1 = net.addSwitch(
        name = "s1"
    )

    net.addLink(h1,s1)
    net.addLink(h2,s1)

    c1 = net.addController(name="c1", ip="192.168.43.191", port=6633)

    s1.start([c1])

    net.build()
    net.start()
    CLI(net)
    net.stop()


if __name__ == '__main__':
    topology()
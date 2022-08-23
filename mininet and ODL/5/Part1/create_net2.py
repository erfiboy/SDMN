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
    name="green2",
    ip="10.0.0.2/24",
    mac="00:00:00:00:00:02",
    )

    h2 = net.addHost(
    name="blue2",
    ip="10.0.0.2/24",
    mac="00:00:00:00:00:02",
    )

    s1 = net.addSwitch(
        name = "s1"
    )

    net.addLink(h1,s1)
    net.addLink(h2,s1)

    net.build()
    net.start()
    CLI(net)
    net.stop()


if __name__ == '__main__':
    topology()
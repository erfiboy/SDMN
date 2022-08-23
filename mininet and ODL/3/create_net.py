from mininet.net import Mininet
from mininet.node import RemoteController, OVSKernelSwitch
from mininet.cli import CLI
from mininet.link import TCLink

def topology(adj_mat, matrix_size):
    net = Mininet(
        controller=RemoteController,
        switch=OVSKernelSwitch,
        link=TCLink
        )

    # Adding hosts
    h1 = net.addHost(
    name="H1",
    ip="10.0.1.1/24",
    mac="00:00:00:00:00:01",
    defaultRoute = "via 10.0.1.1",
    )

    h2 = net.addHost(
    name="H2",
    ip="10.0.2.1/24",
    mac="00:00:00:00:00:02",
    defaultRoute = "via 10.0.2.1",
    )

    switches = []

    for i in range(0,matrix_size):
        switches.append(net.addSwitch(
            name = "s"+str(i+1),
            protocols= "OpenFlow13"
        ))

    net.addLink(switches[0],h1)
    net.addLink(switches[matrix_size-1], h2)
    
    for i in range(1, matrix_size+1):
        for j in range(1, matrix_size+1):
            if adj_mat[i-1][j-1] == 0:
                continue
            net.addLink(switches[i-1],switches[j-1], port1=i*matrix_size+j, port2=i*matrix_size+j)


    c1 = net.addController(name="c1", ip="127.0.0.1", port=6633)

    for switch in switches:
        switch.start([c1])

    net.build()
    net.start()
    CLI(net)
    net.stop()


if __name__ == '__main__':

    matrix_size = int(input("Enter matrix size: "))
    adj_mat = [[] for i in range(0,matrix_size)]
    try:
        for i in range(0, matrix_size):
            for j in range(0, matrix_size):
                adj_mat[i].append(int(input()))
    except Exception as e:
        print e
        print "Error: please enter an integer"
        exit()

    topology(adj_mat, matrix_size)
from mininet.topo import Topo

class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)

        # Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        # Add hosts
        h1 = self.addHost('h1', ip='10.0.0.1/24')
        h2 = self.addHost('h2', ip='10.0.0.2/24')

        # Add links
        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(s1, s2)

topos = {'mytopo': (lambda: MyTopo())}



sudo mn --custom custom_topology.py --topo mytopo --mac --switch ovsk --controller=remote
./pox.py forwarding.l2_learning
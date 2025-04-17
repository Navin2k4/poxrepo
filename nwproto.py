from mininet.topo import Topo

class LinearTopo(Topo):
    def __init__(self, n=2):
        Topo.__init__(self)
        switches = []

        for i in range(n):
            switch = self.addSwitch('s%s' % (i+1))
            host = self.addHost('h%s' % (i+1))
            self.addLink(host, switch)
            switches.append(switch)

        for i in range(n - 1):
            self.addLink(switches[i], switches[i + 1])

topos = {'linear': LinearTopo}

sudo mn --custom linear_topo.py --topo linear --mac --switch ovsk --controller remote
h1 ping h2
h1 python3 -m http.server 80 &
h2 curl h1
h1 tcpdump -i h1-eth0 &
h1 iperf -s &
h2 iperf -c h1

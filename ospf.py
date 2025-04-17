sudo apt-get update
sudo apt-get install mininet quagga quagga-doc

from mininet.net import Mininet
from mininet.node import Node
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel

# Function to add Quagga configuration
def configRouter(router, config_file):
    router.cmd(f'echo 1 > /proc/sys/net/ipv4/ip_forward')
    router.cmd(f'zebra -f {config_file}/zebra.conf -d -z {config_file}/zebra.sock -i {config_file}/zebra.pid')
    router.cmd(f'ospfd -f {config_file}/ospfd.conf -d -z {config_file}/zebra.sock -i {config_file}/ospfd.pid')

def run():
    net = Mininet(link=TCLink)

    # Add hosts and routers
    h1 = net.addHost('h1', ip='10.0.1.2/24', defaultRoute='via 10.0.1.1')
    h2 = net.addHost('h2', ip='10.0.2.2/24', defaultRoute='via 10.0.2.1')
    r1 = net.addHost('r1')
    r2 = net.addHost('r2')
    r3 = net.addHost('r3')

    # Add links
    net.addLink(h1, r1)
    net.addLink(h2, r2)
    net.addLink(r1, r2)
    net.addLink(r2, r3)
    net.addLink(r3, r1)

    net.start()

    # Configure router interfaces
    r1.cmd('ifconfig r1-eth0 10.0.1.1/24')
    r1.cmd('ifconfig r1-eth1 10.0.3.1/24')
    r1.cmd('ifconfig r1-eth2 10.0.5.1/24')

    r2.cmd('ifconfig r2-eth0 10.0.2.1/24')
    r2.cmd('ifconfig r2-eth1 10.0.3.2/24')
    r2.cmd('ifconfig r2-eth2 10.0.4.1/24')

    r3.cmd('ifconfig r3-eth0 10.0.4.2/24')
    r3.cmd('ifconfig r3-eth1 10.0.5.2/24')

    # Load Quagga config (Assume config files are in /etc/quagga/r1, r2, r3 folders)
    configRouter(r1, '/etc/quagga/r1')
    configRouter(r2, '/etc/quagga/r2')
    configRouter(r3, '/etc/quagga/r3')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()


hostname r1
router ospf
 network 10.0.1.0/24 area 0
 network 10.0.3.0/24 area 0
 network 10.0.5.0/24 area 0
 
hostname r1
interface r1-eth0
interface r1-eth1
interface r1-eth2


sudo python3 ospf_mininet.py

r1 vtysh
> show ip ospf neighbor
> show ip ospf route

h1 ping h2

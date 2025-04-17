from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

class Firewall(object):
    def __init__(self):
        core.openflow.addListeners(self)
        self.blocked_ports = [80]  # Block HTTP traffic

    def _handle_ConnectionUp(self, event):
        log.info("Installing firewall rules on switch %s", event.dpid)
        for port in self.blocked_ports:
            msg = of.ofp_flow_mod()
            msg.match.dl_type = 0x0800  # IP packets
            msg.match.nw_proto = 6      # TCP
            msg.match.tp_dst = port     # Destination port
            msg.actions = []            # Drop packet
            event.connection.send(msg)
            log.info("Blocked TCP port %s", port)

def launch():
    core.registerNew(Firewall)


./pox.py log.level --DEBUG openflow.discovery openflow.spanning_tree openflow.of_01 --no-flood firewall
sudo mn --topo single,3 --mac --switch ovsk --controller=remote,ip=127.0.0.1,port=6633
h1 ping h2
h2 python3 -m http.server 80 &
h1 curl 10.0.0.2

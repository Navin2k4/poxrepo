from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.addresses import IPAddr, EthAddr

log = core.getLogger()

class SimpleRouter(object):
    def __init__(self, connection):
        self.connection = connection
        connection.addListeners(self)

        # Static routing table: dst_ip -> (port_number, next_hop_mac)
        self.routing_table = {
            IPAddr("10.0.0.1"): (1, EthAddr("00:00:00:00:00:01")),
            IPAddr("10.0.0.2"): (2, EthAddr("00:00:00:00:00:02")),
            IPAddr("10.0.0.3"): (3, EthAddr("00:00:00:00:00:03")),
        }

    def _handle_PacketIn(self, event):
        packet = event.parsed
        if not packet.parsed:
            log.warning("Incomplete packet. Ignoring.")
            return

        if packet.type == packet.IP_TYPE:
            ip_pkt = packet.payload
            dst_ip = ip_pkt.dstip

            if dst_ip in self.routing_table:
                out_port, next_mac = self.routing_table[dst_ip]

                msg = of.ofp_flow_mod()
                msg.match = of.ofp_match.from_packet(packet)
                msg.actions.append(of.ofp_action_dl_addr.set_dst(next_mac))
                msg.actions.append(of.ofp_action_output(port=out_port))

                self.connection.send(msg)
                log.info(f"Forwarding to {dst_ip} via port {out_port}")
            else:
                log.warning(f"No route for {dst_ip}")

def launch():
    def start_router(event):
        log.info("Router started")
        SimpleRouter(event.connection)
    core.openflow.addListenerByName("ConnectionUp", start_router)

./pox.py forwarding.l2_learning simple_route
sudo mn --topo linear,3 --mac --switch ovsk --controller=remote,ip=127.0.0.1,port=6633

pingall
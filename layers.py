$ sudo mn --topo=single,3 --controller=none –mac  
dump  
net  
sh ovs-ofctl show s1  
sh ovs-ofctl add-flow s1 action=normal  
pingall  
sh ovs-ofctl dump-flows s1  
sh ovs-ofctl del-flows s1

### Using Layer 1

sh ovs-ofctl add-flow s1 priority=500,in_port=1,actions=output:2  
sh ovs-ofctl add-flow s1 priority=500,in_port=2,actions=output:1  
h1 ping -c2 h2  
h3 ping -c2 h2  
sh ovs-ofctl dump-flows s1  
sh ovs-ofctl add-flow s1 priority=32768,action=drop  
h3 ping -c2 h2  
sh ovs-ofctl del-flows s1 --strict  
h3 ping -c2 h2

### Using Layer 2

sh ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:02,actions=output:2  
sh ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:01,actions=output:1  
sh ovs-ofctl add-flow s1 dl_type=0x806,nw_proto=1,action=flood

sh ovs-ofctl dump-flows s1  
sh ovs-ofctl del-flows s1

### Using Layer 3

sh ovs-ofctl add-flow s1
priority=500,dl_type=0x800,nw_src=10.0.0.0/24,nw_dst=10.0.0.0/24,actions=normal  
sh ovs-ofctl add-flow s1
priority=800,dl_type=0x800,nw_src=10.0.0.3,nw_dst=10.0.0.0/24,actions=mod_nw_tos:184, normal  
sh ovs-ofctl add-flow s1 arp,nw_dst=10.0.0.1,actions=output:1  
sh ovs-ofctl add-flow s1 arp,nw_dst=10.0.0.2,actions=output:2  
sh ovs-ofctl add-flow s1 arp,nw_dst=10.0.0.3,actions=output:3  
pingall

sh ovs-ofctl dump-flows s1  
sh ovs-ofctl del-flows s1

### Using Layer 4

h3 python -m SimpleHTTPServer 80 &  
sh ovs-ofctl add-flow s1 arp,actions=normal  
sh ovs-ofctl add-flow s1 priority=500,dl_type=0x800,nw_proto=6,tp_dst=80,actions=output:3  
sh ovs-ofctl add-flow s1 priority=800,ip,nw_src=10.0.0.3,actions=normal  
h1 curl h3

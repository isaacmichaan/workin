from scapy.all import *


for i in range(1, 30):
	pkt = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=f"10.0.0.{i}")
	res = srp1(pkt, timeout=0.5, verbose=0)
	if res:
		print(res['ARP'].psrc, 'is at ', res['ARP'].hwsrc)

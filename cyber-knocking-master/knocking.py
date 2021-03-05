from scapy.all import *
import os

key = "isaacmic"
knocking = []
ok = [[8080, "RA"], [8834, "SA"], [8840, "R"]]

def handler(pkt):
	if pkt.haslayer('TCP') and pkt['IP'].dst=="10.0.2.4":
		knocking.append([pkt['TCP'].dport, pkt.sprintf('%TCP.flags%')])
	if len(knocking) > 3:
		del(knocking[0])
	print(knocking)
	try:
		if sxor(key, pkt['Raw'].load.decode()) and knocking == ok:
			os.system(f"iptables -I INPUT 1 -p tcp -s {pkt['IP'].src} --dport 22 -j ACCEPT")
	except IndexError:
		pass

sniff(filter="tcp and portrange 8000-9000", prn=handler)

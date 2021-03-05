import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from random import randint

dest = input("Enter Ip to scan: ")
#p = input("Enter Port to scan: ")

# option 1
#layer1 = Ether()

#layer2 = IP()
#layer2.dst = dest

#layer3 = TCP()
#layer3.dport = int(p)

# option 2
ports = [22, 80, 7878, 7979, 9090]
for port in ports:
	#pkt = Ether()/IP(dst=dest)/TCP(sport=randint(1000,65000), dport=int(p))
	pkt = Ether()/IP(dst=dest)/TCP(sport=randint(1000,65000), dport=port)
	res = srp1(pkt, timeout=2)
	if res:
		if 'TCP' in res:
			if res['TCP'].flags == "SA":
				print(f"Port {port} is Open")
			elif res['TCP'].flags == "RA":
				print(f"Port {port} is Closed")
	else:
		print(f"No Response PORT: {port}")

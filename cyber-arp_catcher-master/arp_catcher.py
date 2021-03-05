from scapy.all import *


def handler(pkt):
	pkt.show()

sniff(count=10, filter="arp", prn=handler)

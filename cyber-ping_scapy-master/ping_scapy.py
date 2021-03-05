import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

ping = Ether()/IP(dst="10.0.2.4")/ICMP()/Raw()

# id
ping['IP'].id = 2

# filename
ping['Raw'].load = "file1"
srp1(ping, timeout = 1)

# message
ping['Raw'].load = "Hello World"
a = srp1(ping, timeout = 1)

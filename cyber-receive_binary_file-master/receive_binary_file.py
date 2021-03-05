from scapy.all import *

src = '10.0.2.4'
d = {} #dictionary

def handler(pkt):
        try:
                if pkt['Raw'] and pkt['IP'].src != src:
                        #if pkt['Raw'].load == b'Finished':
                                #return 1

                        # save to dict
                        if str(pkt['IP'].id) not in d:
                                d[str(pkt['IP'].id)] = str(pkt['Raw'].load.decode())
                                return

                        # write to file
                        try:
                                f = open(d[str(pkt['IP'].id)], "ab")
                                f.write(pkt['Raw'].load)
                                f.close()
                        except:
                                return handler(pkt)

        except IndexError:
                pass

sniff(prn=handler, filter="icmp")

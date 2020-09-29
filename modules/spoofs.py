from scapy.all import *
import scapy.all
from scapy.layers.inet import srp,Ether,ARP


class spoofs:

    def __init__(self, valueObj):
        self.valueObj = valueObj




    def get_mac(self, ip):
        answeredList = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = ip), timeout = 5, verbose = False)[0]
        return answeredList[0][1].hwsrc
    
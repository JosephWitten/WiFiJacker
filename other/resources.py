import sys

class resource:

    def displayHelp(self):
        print("----- Deauth tool by Joseph Sm9l Witten -----")
        print("- Use ethically with permission -")
        print("")
        print("sudo python3 wifiJacker.py <OPTIONS>")

        print("-h / --help --- shows this help page (OPTIONAL)")
        print("-i / --interface --- select the wifi interface in which to deploy packets (REQUIRED)")
        print("-b / --blacklist --- (Not implemented yet)")
        print("-B / --blacklistFile --- (Not implemented yet)")
        print("-w / --whitelist --- (Not implemented yet)")
        print("-W / --whitelistFile --- (Not implemented yet)")
        print("-c / --count --- specify the amount of deauth packets sent, default 100 (OPTIONAL)")



        sys.exit()

    def displayBasicHelp(self):
        print("sudo python3 wifiJacker.py <OPTIONS>")
        print("'sudo python3 wifiJacker.py --help' for more information")
        sys.exit()
        

    def printSuperValues(self, valueObj):
        print(valueObj.interfaceName + " is the interface name")
        print(valueObj.whitelist + " is whitelisted")
        print(", ".join(valueObj.blacklist) + " is blacklisted")
        print(valueObj.whitelistFile + " is the whitelist file")
        print(valueObj.blacklistFile + " is the blacklist file")


class resource:

    def displayHelp(self):
        print("This is the future help page")

    def printSuperValues(self, valueObj):
        print(valueObj.interfaceName + " is the interface name")
        print(valueObj.whitelist + " is whitelisted")
        print(valueObj.blacklist + " is blacklisted")
        print(valueObj.whitelistFile + " is the whitelist file")
        print(valueObj.blacklistFile + " is the blacklist file")

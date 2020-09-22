import sys
import getopt
from other import resources
from other import values
from modules import deauths

toolBox = resources.resource()
superValues = values.value()

argv = sys.argv[1:]

options, args = getopt.getopt(argv, "hi:b:B:w:W:", ["help", "blacklist=", "interface=", "blacklistFile=", "whitelist=", "whitelistFile="])

print(options, args)

for option, arg in options:
    if option in ["-h", "--help"]:
        toolBox.displayHelp()
    if option in ["-i", "--interface"]:
        superValues.interfaceName = arg
    if option in ["-b", "--blacklist"]:
        superValues.blacklist = arg
    if option in ["-B", "--blacklistFile"]:
        superValues.blacklistFile = arg
    if option in ["-w", "--whitelist"]:
        superValues.whitelist = arg
    if option in ["-W", "--whitelistFile"]:
        superValues.whitelistFile = arg

toolBox.printSuperValues(superValues)












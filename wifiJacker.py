import sys
import getopt
from other import resources
from other import values

toolBox = resources.resource()
superValues = values.value()

argv = sys.argv[1:]

options, args = getopt.getopt(argv, "hi:b:", ["help", "blacklist=", "interface="])

print(options, args)

for option, arg in options:
    if option in ["-h", "--help"]:
        toolBox.displayHelp()
    if option in ["-i", "--interface"]:
        superValues.interfaceName = arg
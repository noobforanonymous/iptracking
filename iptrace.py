import argparse
import requests, json
import sys
from sys import argv
import os

parser = argparse.ArgumentParser()
parser.add_argument("-i", help="target/host IP address", type=str, dest='target', required=True)
args = parser.parse_args()

green = '\033[1;92m'
yellow = '\033[93m'
purple = '\033[35m'
blue = '\033[34m'
clear = '\033[0m'
bold = '\033[01m'

print(green + """

     ____  ______   ________  __________  ___   ____________
   / __ \/_  __/  /  _/ __ \/_  __/ __ \/   | / ____/ ____/
  / /_/ / / /     / // /_/ / / / / /_/ / /| |/ /   / __/   
 / _, _/ / /    _/ // ____/ / / / _, _/ ___ / /___/ /___   
/_/ |_| /_/    /___/_/     /_/ /_/ |_/_/  |_\____/_____/   

""" + green)
print(purple + bold + "   <====YOUTUBE CHANNEL NAME RTHACKS====> \n" + clear)
print(purple+ bold + " <=========https://dev-regaanthamimprogramming.pantheonsite.io/=======> \n" + clear)

ip = args.target
api = "http://ip-api.com/json/"
try:
    data = requests.get(api + ip).json()
    sys.stdout.flush()
    a = blue + bold + "[$]"
    b = bold + "[$]"
    print(a, "[Victim]:", data['query'])
    print(green + "<--------------->" + green)
    print(b, "[ISP]:", data['isp'])
    print(green + "<--------------->" + green)
    print(a, "[Organisation]:", data['org'])
    print(green + "<--------------->" + green)
    print(b, "[City]:", data['city'])
    print(green + "<--------------->" + green)
    print(a, "[Region]:", data['region'])
    print(green + "<--------------->" + green)
    print(b, "[Longitude]:", data['lon'])
    print(green + "<--------------->" + green)
    print(a, "[Latitude]:", data['lat'])
    print(green + "<--------------->" + green)
    print(b, "[Time zone]:", data['timezone'])
    print(green + "<--------------->" + green)
print(blue + """
+-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+ +-+-+-+-+ +-+-+ +-+-+ +-+-+-+-+-+                                    
|T|H|A|N|K|S| |F|O|R| |U|S|I|N|G| |T|H|I|S| |T|O|O|L| |C|O|D|E| |B|Y| |R|T| |H|A|C|K|S|                                    
+-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+ +-+-+-+-+ +-+-+ +-+-+ +-+-+-+-+-+
""" + blue)
except KeyboardInterrupt:
    print('OK Bye' + blue)
    sys.exit(0)
except requests.exceptions.ConnectionError as e:
    print(purple + "[~]" + " TURN ON YOUR INTERNET OR CHECK YOUR INTERNET CONNECTION" + clear)
sys.exit(1)

#Script By Webcns 

import argparse
import requests, json
import sys
from sys import argv
import os



parser = argparse.ArgumentParser()

parser.add_argument ("-v", help= "target/host IP address", type=str, dest='target', required=True )

args = parser.parse_args()


red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'


print (red+"""
               _                    
             | |                   
__      _____| |__   ___ _ __  ___ 
\ \ /\ / / _ \ '_ \ / __| '_ \/ __|
 \ V  V /  __/ |_) | (__| | | \__ \
  \_/\_/ \___|_.__/ \___|_| |_|___/  
  
"""+red)
print (lgreen+bold+"         <===[[ coded by Webcns /Salvadores Team ]]===> \n"+clear)
print (yellow+bold+"   <---(( Instagram:hackin50tonu ))--> \n"+clear)


ip = args.target

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = lgreen+bold+"[$]"
        b = cyan+bold+"[$]"
        print (a, "[Kurban]:", data['query'])
        print(red+"<--------------->"+red)
        print (a, "[Organizasyon]:", data['org'])
        print(red+"<--------------->"+red)
        print (b, "[Sehir]:", data['city'])
        print(red+"<--------------->"+red)
        print (a, "[Bölge]:", data['region'])
        print(red+"<--------------->"+red)
        print (b, "[Boylam]:", data['lon'])
        print(red+"<--------------->"+red)
        print (a, "[Enlem]:", data['lat'])
        print(red+"<--------------->"+red)
        print (b, "[Saat dilimi]:", data['timezone'])
        print(red+"<--------------->"+red)
        print (a, "[Posta kodu]:", data['zip'])
        print (" "+yellow)

except KeyboardInterrupt:
        print ('Sonlandırıcı: Bye'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[~]"+" internet bağlantınızı kontrol edin!"+clear)
sys.exit(1)

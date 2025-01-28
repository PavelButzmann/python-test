#!/usr/bin/env python3

import sys
import ipcalc
import pandas as pd
import numpy as np
from netaddr import IPAddress
from ipaddress import IPv4Address
from termcolor import colored, cprint
from colorama import init, Fore, Back, Style
init()

IP = ipcalc.Network(sys.argv[1])


if len(sys.argv) == 2:
    (addr, cidr) = sys.argv[1].split('/')
        
    addr = [int(x) for x in addr.split(".")]
    cidr = int(cidr)
    mask = [( ((1<<32)-1) << (32-cidr) >> i ) & 255 for i in reversed(range(0, 32, 8))]
elif len(sys.argv) == 3:
    addr = sys.argv[1]
    mask = sys.argv[2]
        
    addr = [int(x) for x in addr.split(".")]
    mask = [int(x) for x in mask.split(".")]
    cidr = sum((bin(x).count('1') for x in mask))
        
IP2 = IPAddress('.'.join(map(str, addr)))

Addre = str(IP2)
netm = str(IP.netmask())
wildc = str(IPv4Address(int(IPv4Address._make_netmask(cidr)[0])^(2**32-1)))
networ = str(IP.network())
broadc = str(IP.broadcast())
Hostmi = str(IP.network()+1) # evaluate to change later
Hostma = str(IP.broadcast()-1) # evaluate to change later
hostsnum = str(IP.size()-2) # evaluate to change later

binaddre = ('.'.join([bin(int(x)+256)[3:] for x in Addre.split('.')]))
binmask = ('.'.join([bin(int(x)+256)[3:] for x in netm.split('.')]))
binwild = ('.'.join([bin(int(x)+256)[3:] for x in wildc.split('.')]))
binnet = ('.'.join([bin(int(x)+256)[3:] for x in networ.split('.')]))
binbrod = ('.'.join([bin(int(x)+256)[3:] for x in broadc.split('.')]))
binhostmi = ('.'.join([bin(int(x)+256)[3:] for x in Hostmi.split('.')]))
binhostma = ('.'.join([bin(int(x)+256)[3:] for x in Hostma.split('.')]))
infor = str(IP.info())

print (" ")  

df = pd.DataFrame({
         "Name": ["Address: ","Netmask: ","Wildcard: "," ","Network: ","Broadcast: ","HostMin: ","HostMax: ","Hosts/Net",],
         "Result": [colored(Addre,"light_blue"), colored(netm,"light_blue"), colored(wildc,"light_blue"), " ", colored(networ,"light_blue"), colored(broadc,"light_blue"), colored(Hostmi,"light_blue"), colored(Hostma,"light_blue"), colored(hostsnum,"light_blue")],
         "Binary": [colored(binaddre,"light_magenta"), colored(binmask,"red"), colored(binwild,"light_magenta"), " ", colored(binnet,"light_magenta"), colored(binbrod,"light_magenta"), colored(binhostmi,"light_magenta"), colored(binhostma,"light_magenta"), colored(infor,"yellow")],
})

print (df.to_string(index=False,header=None))
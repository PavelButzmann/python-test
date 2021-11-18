#!/bin/python3
#---- Script creado por Herr Stiefel
#---- Test de conectividad mediante ping a diferentes direcciones IP

import time
import os
import subprocess
from termcolor import colored
from ipcalc import IP,Network
from datetime import date
from pythonping import ping

today = date.today()

print (" ")
print ("-----------------------------------")
print ("-                                 -")
print (" Por favor utiliza el prefijo CIDR ")
print ("      ejemplo: 192.168.1.0/24      ")
print ("-                                 -")
print ("-----------------------------------")
print (" ")

target = input("Direccion ip del segmento a probar: ") #Se solicita al usuario ingresar la direccion IP con la que se desea probar conectividad
print (" ")
print ("Se realiza ping a segmento "+ str(target))
print (" ")

time.sleep(2) #Sleep for 2 seconds
# ping (target, verbose=True)

for x in Network(target):
	try:
		response = subprocess.check_output(
			['ping','-c','1', str(x)],
			stderr=subprocess.STDOUT,
			universal_newlines=True
		)
		print (x, (colored(("	UP"),'green')))
	except subprocess.CalledProcessError:
		response = None
		print (x, (colored(("	DOWN"),'red')))

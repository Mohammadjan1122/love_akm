#Author Mohammad sultani

import os, platform

try:

   import requests

except:

   os.system('pip2 install requests')

import requests
import platform 
bit = platform.architecture()[0]

if bit == '64bit':
	os.system("git pull")
	from love import menu
	menu()
elif bit == '32bit':
	os.system("git pull")
	from love32 import menu
	menu()



   




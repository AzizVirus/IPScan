# -*- coding: utf-8 -*-
#!/usr/bin/python

import os
import sys
import time
import socket
import random

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'     #Defining Colors
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
start_time = time.time()
prompt = bcolors.FAIL + bcolors.BOLD +  "IPScan Tool >  " + bcolors.ENDC
mainmenu = bcolors.OKBLUE + bcolors.BOLD +  '''

Select A Number:

                      +--------------------------------------+
                      |                                      |
                      |  [1]----- PING Scan ------------ [1] |
                      |  [2]----- Normal Scan ---------- [2] |
                      |  [3]----- Fast Scan ------------ [3] |
                      |  [4]----- OS Detection---------- [4] |
                      |  [5]----- Ports Version Scan---- [5] |
                      |                                      |
                      +--------------------------------------+

''' + bcolors.ENDC

os.system("clear")
time.sleep(0.75)
os.system("figlet IPscan Tool ")
print ("")
print bcolors.OKGREEN + bcolors.BOLD + ("  Tool Powered By Nmap ")
print bcolors.OKGREEN + bcolors.BOLD + ("  Coded By AzizVirus")
print bcolors.OKGREEN + bcolors.BOLD + ("  Report Any Issues On My Github")
print bcolors.OKGREEN + bcolors.BOLD + ("  Github: github.com/AzizVirus") + bcolors.ENDC
time.sleep(0.5)

print mainmenu
choice = raw_input(prompt)
if choice == "1":
 ip = raw_input(prompt + "Select IP / HostName (example: facebook.com):  ")
 packets = raw_input(prompt + "Select Packets Number To Send (0 - 2147483647) Or Press [Enter] For Default 2147483647 ")
 print ("")
 print prompt + ("If There Is A Problem.. Restart The Tool By Typing Ctrl+C ! ")
 print ("")
 os.system("ping "+ip+" -c "+packets)
 print ("")
 print (prompt + "Time Elapsed: "+ str(time.time() - start_time))
 print ("")
elif choice == "2":
 print ("")
 ip = raw_input(prompt + "Select IP / HostName (example: facebook.com):  ")
 print ("")
 print prompt + ("If There Is A Problem.. Restart The Tool By Typing Ctrl+C ! ")
 print ("")
 os.system("nmap "+ip)
 print ("")
 print (prompt + "Time Elapsed: "+ str(time.time() - start_time))
 print ("")
elif choice == "3":
 print ("")
 ip = raw_input(prompt + "Select IP / HostName (example: facebook.com):  ")
 print ("")
 print prompt + ("If There Is A Problem.. Restart The Tool By Typing Ctrl+C ! ")
 print ("")
 os.system("nmap -F "+ip)
 print ("")
 print (prompt + "Time Elapsed: "+ str(time.time() - start_time))
 print ("")
elif choice == "4":
 print ("")
 ip = raw_input(prompt + "Select IP / HostName (example: facebook.com):  ")
 print ("")
 print prompt + ("If There Is A Problem.. Restart The Tool By Typing Ctrl+C ! ")
 print ("")
 os.system("nmap -sV -O "+ip)
 print ("")
 print (prompt + "Time Elapsed: "+ str(time.time() - start_time))
 print ("")
elif choice == "5":
 ip = raw_input(prompt + "Select IP / HostName (example: facebook.com):  ")
 print ("")
 print prompt + ("If There Is A Problem.. Restart The Tool By Typing Ctrl+C ! ")
 print ("")
 os.system("nmap -sV "+ip)
 print ("")
 print (prompt + "Time Elapsed: "+ str(time.time() - start_time))
 print ("")
else:
 print ("")
 print ("Choose A Number 0 - 5  Exit... ")
 print ("")
 sys.exit()



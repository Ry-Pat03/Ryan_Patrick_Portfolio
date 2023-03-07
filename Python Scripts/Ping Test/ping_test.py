#!/usr/bin/python3
#-* coding: utf-8 -*-

#Author: Ryan Patrick
#Most Recent Date Changed: 2/9/2023


#Four main goals
#1.) Test connectivity to gateway
#2.) Test connectivity to a remote IP address
#3.) Test for DNS resolution
#4.) Display gateway and IP address

#imports
import os
import time
import netifaces
import subprocess
from colorama import Fore, Back, Style


#Function for startup
def startup():
	os.system('clear')
	print("	-----------------------------------------")
	print("	|	" + Style.BRIGHT + Fore.CYAN + "Ping Test Troubleshooter" +
	Style.RESET_ALL + "	|")
	print("	-----------------------------------------")
	print("\n")
	print("Please make a selection:" + "\n")
	print("\t" + "1 - Test connectivity to your gateway.")
	print("\t" + "2 - Test for remote connectivity.")
	print("\t" + "3 - Test for DNS resolution.")
	print("\t" + "4 - Display gateway IP Address.")
	print("\n")



#Function to gather the user's choice
def getChoice():
	test = input("Please enter a " + Style.BRIGHT + Fore.CYAN + "number (1-4) " 
	+ Style.RESET_ALL + "or " + Style.BRIGHT + Fore.CYAN + "'Q/q'" + Style.RESET_ALL 		+ " to quit the program.  ")
	os.system('clear')
	return test



#Function for gateway connectivity test (1)
def gateway():
	#Setup for gateway test
	print("Testing connectivity to your " + Style.BRIGHT + Fore.YELLOW + "gateway" + 		Style.RESET_ALL + ".")
	time.sleep(4)
	os.system('clear')
	print("Running test, please wait..." + "\n")
	time.sleep(3)
	
	
	#Try and except for TypeError if gateway = NoneType (this happens when network is 		disconnected)
	try:
		#Gather gateway address
		gateway = netifaces.gateways().get('default').get(2)[0]
	
		#ping gateway address
		ping = os.system("ping -c 4  " + gateway + ">/dev/null")		
	
		#Output depening on response

		if(ping == 0):
			print("Please inform your system admin the test was a " + Style.BRIGHT + 				Fore.GREEN + "SUCCESS" + Style.RESET_ALL + "!")
			time.sleep(3)
		else:
			print("Please inform your system admin the test was a " + Fore.RED +
 			"FAILURE" + Style.RESET_ALL + ". :(") 
			time.sleep(3)
	except TypeError:
		print("Please inform your system admin the test was a " + Fore.RED +
 		"FAILURE" + Style.RESET_ALL + ". :(") 
		time.sleep(3)
	
	

#Function for remote IP test (2)
def remote():
	#Setup for remote IP test
	print("Testing for " + Style.BRIGHT + Fore.YELLOW + "remote connectivity"
	+ Style.RESET_ALL + "... trying IP address " + Style.BRIGHT + Fore.YELLOW 
	+ "129.21.3.17" + Style.RESET_ALL + "." + "\n")
	remote = "129.21.3.17"
	
	#ping remote address
	ping = os.system("ping -c 4  " + remote + ">/dev/null 2>&1")
	time.sleep(3)

	#Output depening on response
	if(ping == 0):
		print("Please inform your system admin the test was a " + Style.BRIGHT + 			Fore.GREEN + "SUCCESS" + Style.RESET_ALL + "!")
		time.sleep(3)
	else:
		print("Please inform your system admin the test was a " + Fore.RED + "FAILURE" + 			Style.RESET_ALL + ". :(") 
		time.sleep(3)



#Function for DNS test using subprocess (3)
def dns():
	#Setup for DNS test
	print("Resolving DNS: trying URL... " + Style.BRIGHT + Fore.YELLOW + " www.google.com" 		+ Style.RESET_ALL + ".")
	dns = "google.com"
	cmd = "ping -c 4 " + dns
	time.sleep(4)
	os.system('clear')
	print("Running test, please wait..." + "\n")
	time.sleep(3)
	
	#Test connection to DNS with subprocess
	output = subprocess.getoutput(cmd)
	
	if("0% packet loss" in output):
		print("Please inform your system admin the test was a " + Style.BRIGHT + 			Fore.GREEN + "SUCCESS" + Style.RESET_ALL + "!")
		time.sleep(3)
	else:
		print("Please inform your system admin the test was a " + Fore.RED + "FAILURE" + 			Style.RESET_ALL + ". :(") 
		
		time.sleep(3)


#Function for displaying gateway and IP (4)
def displayIP():
	#Try and except for TypeError if gateway = NoneType
	try:
		#Get Gateway IP Address
		gateway = netifaces.gateways().get('default').get(2)[0]

		#Display the gateway
		print("Your gateway IP Address is " + Style.BRIGHT + Fore.YELLOW + gateway +
		Style.RESET_ALL + ".")
		time.sleep(4)

	except TypeError:
		print("Unable to connect to your gateway." + "\n" +  
		"Please inform your system admin the test was a " + Fore.RED + "FAILURE" 
		+ Style.RESET_ALL + ". :(")
		time.sleep(4)
	


#Function for quiting 
def quit():
	print("Quitting script. Returning to shell..." + "\n")
	print(Style.BRIGHT + Fore.CYAN + "Have a great day :)" + Style.RESET_ALL)
	time.sleep(3)
	os.system('clear')



#Main function to put all the pieces together
def main():
	#Start the startup prompts
	startup()

	#Gather input and set flag
	test = getChoice()
	flag = True

	#Decide what test the user wants with while loop
	while(flag == True):
		if(test == "q" or test == "Q"):
			quit()
			break
		else:
			
			if(test == "1"):
				gateway()
				startup()
				test = getChoice()

			elif(test == "2"):
				remote()
				startup()
				test = getChoice()

			elif(test == "3"):
				dns()
				startup()
				test = getChoice()
			
			elif(test == "4"):
				displayIP()
				startup()
				test = getChoice()

			else:
				print("You entered an " + Style.BRIGHT + Fore.RED 
				+ "invalid option" + Style.RESET_ALL + "!" + "\n")
				print("Please enter a " + Style.BRIGHT + Fore.RED + 
				"valid number (1-4)" + Style.RESET_ALL + " or " + Style.BRIGHT 					+ Fore.RED + "Q/q" + Style.RESET_ALL + " to quit.")
				time.sleep(3)
				startup()
				test = getChoice()	
	


#Running of the script
if __name__ == '__main__':
	main()

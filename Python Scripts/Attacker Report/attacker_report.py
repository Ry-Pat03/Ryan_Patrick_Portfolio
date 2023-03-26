#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Author: Ryan Partick
#Most Recent Date Modified: 3/25/23

#Goals for Script

#FOR EACH IP with attmepts >= 10 IN FILE
#1.) Show IP Addresses
#2.) Number of failed login attempts
#3.) Country of Origin
#5.) Reports Date (Just once)

#Imports
import os
import re
import subprocess
from colorama import Fore, Back, Style
#To install geoip, execute the following in the terminal
	#python3 -m pip install python-geoip-python3
	#python3 -m pip install python-geoip-geolite2
from geoip import geolite2
from pathlib import Path

#Global Styling Variables
red = Style.BRIGHT + Fore.RED
green = Style.BRIGHT + Fore.GREEN
reset = Style.RESET_ALL

#Functions

#Function for Checking/Reading files and returning a list of all the lines with an IP address and failures
def checkLog(file):
	#Check file and create list
	ips = []
	path = ""

	for dirpath, dirname, filename in os.walk("/"):

		#If file is there
		if file in filename:
			path = os.path.join(dirpath, file)

			#Look for IPs in file and add to string
			with open(file) as log:
				logstr = log.readlines()

			#Add IPs to the list
			for line in logstr:

				if (re.search("Failed password",line) != None):
					ips.append(line)

#				### I Chose to decide an attack based on 'Failed password' #				since that is the suspicious error and 
#				the most common forms of attacks that show up in this #				log ###
			#print(ips)

			#If file isn't there
			if(path == ""):
				print("File not found :(")
	
	return ips


#Function for parsing through IP list
def ipParser(ips):
	#Create dictonary that will be used to track IPs and their attempts
	ipDict = {}
	num = 0

	#Create the IP pattern we're looking for with re
	pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

	
	#Look for IPs and add them to dictonary
	for i in ips:
		
		index = re.search(pattern,i)
		
		if index:
			ip = index[0]
			ipDict[ip] = 0
		
	#Look through the dictonary and see how many times the IPs appear
	for ip in ipDict:
		num = 0
		for i in ips:
			valid = re.search(ip, i)
			if valid != None:
				num += 1
		ipDict[ip] = num
	
	#Return dictonary for use in other function
	return ipDict


#Function for figuring out IP Country and Display
def ipCountry(ipDict):
	#Display the header of the output first
	date = subprocess.run(['date', '+%B %d'],stdout=subprocess.PIPE,stderr=subprocess.DEVNULL).stdout.decode('utf-8')
	date = date.strip("\n")
	year = subprocess.run(['date', '+%Y'],stdout=subprocess.PIPE,stderr=subprocess.DEVNULL).stdout.decode('utf-8')
	print(green + "Attacker Report " + reset + "- "+ date + ", " + year)
	print(red + "COUNT 	IP ADDRESS	COUNTRY" + reset) 

	#Sort dictonary in accending order
	sortedIpDict = dict(sorted(ipDict.items(), key=lambda item: item[1]))
	numList = list(sortedIpDict.items())

	#Remove the IPs with less then 10 failures
	for ip in numList:
		if ip[1] <= 10:
			#Get key in order pop from dictonary
			#This looks complicated, but since I only knew the value I had to make both the keys 				and values of sortedIpDict into lists and then get the key using the value that was 				less than or equal to 10
			key = list(sortedIpDict.keys())[list(sortedIpDict.values()).index(ip[1])]
			sortedIpDict.pop(key)
	
	#Find the country for each IP and display
	for ip in sortedIpDict:
		ipmatch = geolite2.lookup(ip)
		country = ipmatch.country
		
		#Final Print
		print(str(sortedIpDict[ip]) + "\t" + ip + "\t" + country)



#Main function
def main():
	#First, check file and gather IP list
	ips = checkLog("syslog.log")
	
	#Second, get the count for the IPs
	ipDict = ipParser(ips)

	#Finally, find the country per IP and display
	ipCountry(ipDict)




#Running of main function
if __name__ == "__main__":
	main()

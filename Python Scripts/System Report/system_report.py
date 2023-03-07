#!/usr/bin/python3
# -*- coding: utf -*-
#Author - Ryan Patrick
#Date last modified - 2/23/23
#Goals for script
#1.) Gather device info (Hostname, Domain)
#2.) Gather network info (IP, Gateway, Network Mask, DNS1, DNS2)
#3.) Gather OS info (Operating System, Operating Version, Kernel Version)
#4.) Gather Storage info (Hard Drive Capacity, Available Space)
#5.) Gather Processor Information (CPU Model, Number of Processors, Number of cores)
#6.) Gather Memory info (Total RAM, Available RAM)
#7.) DIRECT OUTPUT TO FILE IN USERS HOME DIRECTORY TITLED "hostname_system_report.log" (DONT HARD CODE HOSTNAME) 

#imports
import os
import platform
import subprocess
#install netifaces 
import netifaces
from colorama import Fore, Back, Style

#Global Variables
reset = Style.RESET_ALL
green = Style.BRIGHT + Fore.GREEN
red = Style.BRIGHT + Fore.RED

#Get Hostname (So it can be written to the file and used in other functions)
shortname = subprocess.run(['hostname','-s'],stdout=subprocess.PIPE,stderr=subprocess.DEVNULL).stdout.decode('utf-8')
hostname = shortname.split('\n')[0]

#CREATE LOG FILE
file = open(hostname + "_system_report.log", "x")
file.close()


#Functions

#Function for device info
def deviceInfo():

  #Get Domain name
  domain = subprocess.run(['domainname'],stdout=subprocess.PIPE,stderr=subprocess.DEVNULL).stdout.decode('utf-8')

  #Print results
  print(green + "Device Information" + reset)
  print("Hostname: " + "\t" + "\t" + hostname)
  print("Domain: " + "\t" + "\t" + domain)

  #Write results
  file = open(hostname + "_system_report.log", "a")
  file.write("Device Information" + "\n" "Hostname: " + "\t" + "\t" + hostname + "\n" + "Domain: " + "\t" + "\t" + domain + "\n")
  file.close()

#Function for network info
def networkInfo():
  #Get IP address
  interface = subprocess.run(['ifconfig', 'ens192'],stdout=subprocess.PIPE,stderr=subprocess.DEVNULL).stdout.decode('utf-8')
  ipBlob = interface.split(" ")
  i = 0
  while(i < len(ipBlob)):
    ip = ipBlob[i]
    if(ip == "inet"):
      ip = (ipBlob[i + 1])
      break
    else:
      i = i + 1

  #Get Gateway
  gateway = netifaces.gateways().get('default').get(2)[0]
  
  #Get Network Mask
  x = 0
  while(x < len(ipBlob)):
    netmask = ipBlob[x]
    if(netmask == "netmask"):
      netmask = (ipBlob[x + 1])
      break
    else:
      x = x + 1

  #Get DNS(s)
  dnsProcess = subprocess.Popen(['cat','/etc/resolv.conf'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  stdout = dnsProcess.communicate()
  dns = str(stdout[0])
  dnsSplit = dns.split(" ")
  dns1 = dnsSplit[5]
  dns2 = dnsSplit[6]
  rightDNS1 = ""
  rightDNS2 = ""
  y = 0
  z = 0

  #I know there has to be a better way to do this but this was the only work around for the \
  #that I could find

  #DNS1
  while(y < len(dns1)):
    if(dns1[y] == "0" or dns1[y] == "1" or dns1[y] == "2" or dns1[y] == "3" or dns1[y] == "4" or dns1[y] == "5" or dns1[y] == "6" or dns1[y] == "7" or dns1[y] == "8" or dns1[y] == "9" or dns1[y] == "."):
      rightDNS1 += dns1[y]
      y += 1
    else:
      break

  #DNS2
  while(z < len(dns2)):
    if(dns2[z] == "0" or dns2[z] == "1" or dns2[z] == "2" or dns2[z] == "3" or dns2[z] == "4" or dns2[z] == "5" or dns2[z] == "6" or dns2[z] == "7" or dns2[z] == "8" or dns2[z] == "9" or dns2[z] == "."):
      rightDNS2 += dns2[z]
      z += 1
    else:
      break

  #Print results
  print(green + "Network Information" + reset)
  print("IP Address: " + "\t" + "\t" + ip)
  print("Gateway: " + "\t" + "\t" + gateway)
  print("Network Mask: " + "\t" + "\t" + netmask)
  print("DNS1: " + "\t" + "\t" + "\t" + rightDNS1)
  print("DNS2: " + "\t" + "\t" + "\t" + rightDNS2 + "\n")

  #Write results
  file = open(hostname + "_system_report.log", "a")
  file.write("Network Information" + "\n" + "IP Address: " + "\t" + "\t" + ip + "\n" + "Gateway: " + "\t" + "\t" + gateway + "\n" "Network Mask: " + "\t" + "\t" + netmask + "\n" + "DNS1: " + "\t" + "\t" + "\t" + rightDNS1 + "\n" + "DNS2: " + "\t" + "\t" + "\t" + rightDNS2 + "\n")
  file.close()


#Function for OS Info
def osInfo():
  #Get OS
  os = platform.linux_distribution()[0]
 
  #Get Operating Version
  version = platform.linux_distribution()[1]
  
  #Get Kernal Version
  kernal = subprocess.run(['uname','-r'],stdout=subprocess.PIPE,stderr=subprocess.DEVNULL).stdout.decode('utf-8')

  #Print Results
  print(green + "OS Information" + reset)
  print("Operating System: " + "\t" + os)
  print("Operating Version: " + "\t" + version)
  print("Kernal Version: " + "\t" + kernal + "\n")

  #Write Results
  file = open(hostname + "_system_report.log", "a")
  file.write("\n" + "OS Information" + "\n" + "Operating System: " + "\t" + os + "\n" + "Operating Version: " + "\t" + version + "\n" +"Kernal Version: " + "\t" + kernal + "\n")
  file.close()


#Get Storage Info
def storageInfo():
  #Get Storage Process
  storage = subprocess.run(['df', '/dev/mapper/rl-root','-H'],stdout=subprocess.PIPE,stderr=subprocess.DEVNULL).stdout.decode('utf-8')
  storageBlob = storage.split(" ")
  
  #Get Total Storage
  totalStorage = storageBlob[20]
  
  #Get Avliable Storage
  availStorage = storageBlob[25]
  
  #Print Results
  print(green + "Storage Information" + reset)
  print("Hard Drive Capacity: " + "\t" + totalStorage)
  print("Avaliable Storage: " + "\t" + availStorage + "\n")

  #Write Results
  file = open(hostname + "_system_report.log", "a")
  file.write("Storage Information" + "\n" + "Hard Drive Capacity: " + "\t" + totalStorage + "\n" + "Avaliable Storage: " + "\t" + availStorage + "\n")
  file.close()


#Get CPU Info
def cpuInfo():
  #GET CPU Process
  cpuProcess =((subprocess.check_output('lscpu', shell=True).strip()).decode())
  cpuBlob = cpuProcess.split('\n')
 
  #Get Model Name
  model = cpuBlob[12]
  x = 0
  rightModel = ""
  while(x < len(model)):
    if(model[x] == "0" or model[x] == "1" or model[x] == "2" or model[x] == "3" or model[x] == "4" or model[x] == "5" or model[x] == "6" or model[x] == "7" or model[x] == "8" or model[x] == "9" or model[x] == "@"):
      
      x += 1
    
    else:
      rightModel += model[x]
      x +=1
  rightModel = rightModel.split()
  rightModel = rightModel[2] + " " + rightModel[3] + " " + rightModel [4]

  #Get CPU Processors
  processors = subprocess.run(['nproc','--all'],stdout=subprocess.PIPE,stderr=subprocess.DEVNULL).stdout.decode('utf-8')
  processors = processors.strip(" ").split()
  processors = processors[0]


  #Get Number of Cores
  cores = cpuBlob[6]
  cores = cores.strip(" ").split()
  cores = cores[3]


  #Print Results
  print(green + "CPU Information" + reset)
  print("CPU Model: " + "\t" + "\t" + rightModel)
  print("Number of Processors: " + "\t" +  processors)
  print("Number of Cores:" + "\t" + cores + "\n")

  #Write Results
  file = open(hostname + "_system_report.log", "a")
  file.write("\n" + "CPU Information" + "\n" + "CPU Model: " + "\t" + "\t" + rightModel + "\n" + "Number of Processors: " + "\t" +  processors + "\n" + "Number of Cores:" + "\t" + cores + "\n")
  file.close()


#Get RAM Info
def ramInfo():
  #Get RAM Process  
  ram = processors = subprocess.run(['free','-h'],stdout=subprocess.PIPE,stderr=subprocess.DEVNULL).stdout.decode('utf-8')
  ram = ram.strip(" ").split()

  #Get Total RAM
  totalRAM = ram[7]

  #Get Available RAM
  availRAM = ram [9]

  #Print Results
  print(green + "Memory Information" + reset)
  print("Total RAM: " + "\t" + "\t" + totalRAM)
  print("Available RAM:" + "\t" + "\t" + availRAM + "\n")

  #Write Results
  file = open(hostname + "_system_report.log", "a")
  file.write("\n" + "Memory Information" + "\n" + "Total RAM: " + "\t" + "\t" + totalRAM + "\n" + "Available RAM:" + "\t" + "\t" + availRAM + "\n")
  file.close() 

#main
def main():
  #Clear termial
  os.system('clear')

  #Get date
  date = subprocess.run(['date','+%D'],stdout=subprocess.PIPE,stderr=subprocess.DEVNULL).stdout.decode('utf-8')
  
  #Print date
  print("\t" + "\t" + red + "System Report - " + date + reset)

  #Write date
  file = open(hostname + "_system_report.log", "a")
  file.write("\t" + "\t" + "System Report - " + date + "\n")
  file.close()

  #Run the rest of the program
  deviceInfo()
  networkInfo()
  osInfo()
  storageInfo()
  cpuInfo()
  ramInfo()
 

#Running of the script
if __name__ == '__main__' :
  main()


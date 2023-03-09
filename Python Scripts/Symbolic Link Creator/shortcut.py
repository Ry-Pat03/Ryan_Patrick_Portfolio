#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Author: Ryan Partick
#Most Recent Date Modified: 3/9/23

#Goals for Script
#1.) Create a shortcut in your home/Desktop directory via user input
#2.) Remove a shortcut from you home/Desktop directory via user input
#3.) Run shortcut report by displaying all shortcuts in the home directory

#Imports
import os
import pathlib
import time
import subprocess
from pathlib import Path
from colorama import Fore, Back, Style

#Global Styling Variables
cyan = Style.BRIGHT + Fore.CYAN
red = Style.BRIGHT + Fore.RED
green = Style.BRIGHT + Fore.GREEN
yellow = Style.BRIGHT + Fore.YELLOW
reset = Style.RESET_ALL

#Helper Functions

#startup Function
def startup():
	os.system('clear')
	print("	-----------------------------------------------")
	print("	|	" + cyan + "\t" + "Shortcut Creator" +
	reset + "	      |")
	print("	-----------------------------------------------")
	print("\n")
	#Print Current directory
	current = Path.home()
	current = str(current)
	print("Your current directory is " + cyan + current + reset + "." + "\n" + "\n")
	print("Please make a selection:" + "\n")
	print("\t" + "1 - Create a shortcut in your Desktop.")
	print("\t" + "2 - Remove a shortcut from your Desktop.")
	print("\t" + "3 - Run shortcut report.")
	print("\n")

#Function for Creating Shortcut
def createShortcut():
	os.system('clear')
	
	#Gather what file user wants to make a shortcut to
	file = input("Please enter the file name to create shortcut: " + "\t")
	
	#Search for file
	path = ""
	for dirpath, dirname, filename in os.walk("/"):
		if file in filename:
			path = os.path.join(dirpath, file)
			#See if user wants to create a shortcut
			confirm = input("Found " + green + path + reset + 
			". Select " + green + "Y/y" + reset + " to create shortcut.   ")
	
			#Check Confirm
			if(confirm == "y" or confirm == "Y"):
			#Create shortcut
				print("Creating Shortcut, please wait...")
				os.system('ln -s ' + path + ' Desktop/' + file )
				time.sleep(3)
				print("Shortcut created! Returning to Main Menu...")
				time.sleep(3)
				break
	if(path == ""):
		print(red + "File not found :(" + '\n' + "Please enter a valid file." 			+ reset)
		time.sleep(3)


#Function for Removing Shortcut
def removeShortcut():
	os.system('clear')

	#Gather what shortcut user wants to remove
	file = input("Please enter the shortcut/link to remove: " + "\t")

	#Check file
	
	
	if(os.path.exists("Desktop/" + file) == True):
		#Get confirmation
		confirm = input("Are you sure you want to remove " 
		+ green + file + reset + "? Press " 
		+ green + "Y/y" + reset + " to confirm: " + "\t")

		#Check Confirm
		if(confirm == "y" or confirm == "Y"):
			print("Removing shortcut, please wait...")
			#Remove shortcut
			os.system('rm Desktop/' + file)
			print("Shortcut removed! Returning to Main Menu...")
			time.sleep(3)
	
	else:
		print("Sorry, couldn't find " + red + file + reset + "\n" 
		+ "Returning to Main Menu...")
		time.sleep(3)

	
#Function for Displaying Shortcuts
def displayShortcuts():
	#Setup
	print("	-----------------------------------------------")
	print("	|	" + cyan + "\t" + "Shortcut Report" +
	reset + "	              |")
	print("	-----------------------------------------------")
	print("\n")

	#Print Current directory
	current = Path.home()
	current = str(current)
	print("Your current directory is " + yellow + current + reset + "." + "\n")

	#Find all shortcuts in Desktop/ and add them to the dictonary + set counter
	links = {}
	i = 0

	for shortcut in os.listdir("Desktop"):
		path = os.path.realpath("Desktop/" + shortcut)
		links[shortcut] = path
		i += 1
	
	#Display Number of links and link info
	i = str(i)
	print("The number of links is " + yellow + i + reset + "." + "\n")
	print(yellow + "\u0332".join(" Symbolic Link") + "\t" + "\t"
	+ "\u0332".join(" Target Path") + reset)

	for link in links:
		print(" "+ link + "\t" + "\t" + links[link])

	#Gather input from user
	choice = input("\n" + "To return to the " + yellow + "Main Menu" + reset + ", press " 
	+ yellow + "Enter" + reset + ". Or select " + yellow + "R/r" 
	+ reset + " to remove a link.")
	
	#Return to main if pressed enter
	if(choice == ""):	
		os.system('clear')
		print("Returning to Main Menu...")
		time.sleep(3)

	#Remove links if R/r is chosen
	elif(choice == "R" or choice == "r"):
		removeShortcut()

	

	


#Function to gather the user's choice
def getChoice():
	choice = input("Please enter a " + cyan + "number (1-3) " 
	+ reset + "or " + cyan + "'Q/q'" + reset 
	+ " to quit the program.  ")
	os.system('clear')
	return choice


#Function for quiting 
def quit():
	print("Quitting script. Returning to shell..." + "\n")
	print(cyan + "Have a great day :)" + reset)
	time.sleep(3)
	os.system('clear')




def main():
	#Start the startup prompts
	startup()

	#Gather input and set flag
	choice = getChoice()
	flag = True

	#Decide what test the user wants with while loop
	while(flag == True):
		if(choice == "q" or choice == "Q" or choice == "quit"):
			quit()
			break
		else:
			
			if(choice == "1"):
				createShortcut()
				startup()
				choice = getChoice()

			elif(choice == "2"):
				removeShortcut()
				startup()
				choice = getChoice()

			elif(choice == "3"):
				displayShortcuts()
				startup()
				choice = getChoice()

if __name__ == "__main__":
	main()

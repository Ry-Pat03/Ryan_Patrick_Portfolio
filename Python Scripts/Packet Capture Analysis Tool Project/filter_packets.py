#Written by Ryan Patrick
import sys

def filter(fileName):
    #Obtain Node Number
    number = fileName[13]

    #Set up the file writing/reading
    start = "No.     Time           Source                Destination           Protocol Length Info"
    f = open(fileName, 'r')
    lines = f.readlines()
    indexes = []
    filtered = open("Node" + number+ "_filtered.txt", 'w')

    #Get all the starting ICMP pings into a list
    for line in lines:
        if '(ping)' in line:
            index = lines.index(line)
            indexes.append(index)

    #Write the data from the ICMP pings
    for index in indexes:
        i = 1
        x = 2
        line = lines[index]
        filtered.write(start + '\n' + line)
        while x > 0:
            line = lines[index + i]
            if line == '\n':
                x -= 1
            filtered.write(line)
            i += 1
                 
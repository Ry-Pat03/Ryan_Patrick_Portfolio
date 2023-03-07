#Written by Tristan Barber
def parse(filename):
	f = open(filename,'r')
	#Things that will be returned:
	wholeData = []
	packets = []
	packetStartIndexes = []
	indexTrack = 0
	#Actual loop that goes through every packet and strips and puts them into a big list
	for line in f:
		#Find where packet begins
		if(line[0:2] == "No"):
				packetStartIndexes.append(indexTrack)
		line = line.strip()
		line = line.split()
		wholeData.append(line)
		indexTrack+=1
	#References the packetStartIndexes and puts the packets into a big list with each element being a packet
	next = 1
	for index in packetStartIndexes:
		packet = []
		try:
			for num in range(index, packetStartIndexes[next]):
				packet.append(wholeData[num])
			next+=1
		except IndexError:
			for num in range(index, len(wholeData)):
				packet.append(wholeData[num])
		packets.append(packet)
			
	print('called parse function in packet_parser.py')
	
	return packets

#parse("Captures/example.txt")
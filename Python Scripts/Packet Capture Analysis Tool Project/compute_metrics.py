#Written by Owen Armstrong

import packet_parser

def compute(parsed: list, node_ip: str, node_no: int) :
	#inputs should be arrays

	print('called compute function in compute_metrics.py')
	
	"""To be computed:
	Data size metrics:
		Number of echo requests sent
		Number of echo requests recieved
		Number of echo replies sent
		Number of echo replies recieved
		Total echo request bytes sent
		Total echo request bytes recieved
		Total echo request data sent
		Total echo request data recieved
	
	Time metrics:
		Average ping round trip time (MS)
		Echo request throughput (kB/s)
		Echo request goodput (kB/s) (ICMP requests total/RTT total)
		Avg. Reply delay (mS)
	
	Distance metric:
		Avg. number of hops per request"""

	erqs = 0
	erqr = 0
	erps = 0
	erpr = 0
	erqbs = 0
	erqbr = 0
	erds = 0
	erdr = 0
	roundtrip = 0
	throughput = 0
	goodput = 0
	delay = 0
	hops = 0
	stotal = 0
	rtotal = 0
	rqtotal = 0
	rptotal = 0

	for i in range(0, len(parsed)):
		if parsed[i][1][2] == node_ip:	#sent metrics
			if parsed[i][1][8] == "request":
				erqs += 1
				erqbs += int(parsed[i][1][5])
				rqtotal += 1
			if parsed[i][1][8] == "reply":
				erps += 1
				delay += int(parsed[i][1][14][:-1])
				hops += (128-int(parsed[i][1][11][4:]))
				rptotal += 1
			for i2 in range(3, len(parsed[i])):
				for i3 in range(1, (len(parsed[i][i2])-1), 2):
					erds += 1
			roundtrip += int(parsed[i][1][14][:-1])
			stotal += 1

		if parsed[i][1][3] == node_ip:	#recieved metrics
			if parsed[i][1][8] == "request":
				erqr += 1
				erqbr += int(parsed[i][1][5])
				rqtotal += 1
			if parsed[i][1][8] == "reply":
				erpr += 1
				delay += int(parsed[i][1][14][:-1])
				hops += (128-int(parsed[i][1][11][4:]))
				rptotal += 1
			for i2 in range(3, len(parsed[i])):
				for i3 in range(1, (len(parsed[i][i2])-1), 2):
					erdr += 1
			roundtrip += int(parsed[i][1][14][:-1])
			rtotal += 1
	
	goodput = rtotal/roundtrip
	tmp = roundtrip
	roundtrip = (tmp/(rtotal+stotal))/1000000
	tmp = delay
	delay = (tmp/rtotal)/1000000
	tmp = hops
	hops = tmp/rtotal

	print("Node #", node_no, ":\n")
	print("Echo Requests Sent, Echo Requests Received, Echo Replies Sent, Echo Replies Received\n\t", erqs, ",", erqr, ",", erps, ",", erpr)
	print("Echo Request Bytes Sent (bytes), Echo Request Data Sent (bytes)\n\t", erqbs, ",", erds)
	print("Echo Request Bytes Received (bytes), Echo Request Data Received (bytes)\n\t", erqbr, ",", erdr, "\n")
	print("Average RTT (milliseconds): ", roundtrip)
	print("Echo Request Throughput (kB/sec): ", throughput)
	print("Echo Request Goodput (kB/sec): ", goodput)
	print("Average Reply Delay (microseconds): ", delay)
	print("Average Echo Request Hop Count: ", hops, "\n\n")

compute(packet_parser.parse("Node1_filtered.txt"), "192.168.100.1", 1)
#!/bin/bash

#Look at phone to see what to run
#do ifconfig to get broadcast ip then ping -b <broadcas ens33> to get recieving ip
ip="192.168.183.2"
time=5
i=1
spawn ()
{
	$echo ifstat -d 1
	$echo ./APM1 $ip &
	PSID1=$!
	$echo ./APM2 $ip &
	PSID2=$!
	$echo ./APM3 $ip &
	PSID3=$!
	$echo ./APM4 $ip &
	PSID4=$!
	$echo ./APM5 $ip &
	PSID5=$!
	$echo ./APM6 $ip &
	PSID6=$!
	#Output files
	echo "Time,APM1 CPU,APM1 Memory" > APM1_metrics.csv
	echo "Time,APM2 CPU,APM2 Memory" > APM2_metrics.csv
	echo "Time,APM3 CPU,APM3 Memory" > APM3_metrics.csv
	echo "Time,APM4 CPU,APM4 Memory" > APM4_metrics.csv
	echo "Time,APM5 CPU,APM5 Memory" > APM5_metrics.csv
	echo "Time,APM6 CPU,APM6 Memory" > APM6_metrics.csv
	echo "seconds,RX data rate,TX data rate,disk writes,available disk capacity" > system_metrics.csv
}

system_metrics ()
{
	#Network data:
	RX=$(ifstat ens33 | grep ens33 | awk -F '  +' '{print $4} ' | cut -d ' ' -f 2)
	TX=$(ifstat ens33 | grep ens33 | awk -F '  +' '{ print $5} ' | cut -d ' ' -f 2)
	RX=${RX%?}
	TX=${TX%?}
	#Disk Data:
	DSK_U=$(df -hm | awk 'FNR == 6 {print $4}')
	#DSK_U=${DSK_U%?} would just remove the unit
	DSK_W=$(iostat -d /dev/sda | awk 'FNR == 4 {print $4}')
	DSK_W=${DSK_W%?}
	echo "$time,$RX,$TX,$DSK_W,$DSK_U" >> system_metrics.csv
}

process_metrics () 
{
	#Gather metrics
	while [ $i -lt 7 ]
	do
		cpu=$(ps -C APM$i -o %cpu | $echo tail -1 | tr -d ' ')
		mem=$(ps -C APM$i -o %mem | $echo tail -1 | tr -d ' ')
		echo "$time,$cpu,$mem" >> APM$i"_metrics".csv
		(( i++ ))
	done
	if [ $i -eq 7 ]
	then
		i=1
	fi
}

cleanup ()
{
	pkill 'ifstat'
	kill -9 $PSID1
	kill -9 $PSID2 
	kill -9 $PSID3
	kill -9 $PSID4
	kill -9 $PSID5
	kill -9 $PSID6
}
trap cleanup EXIT
#Cobalt mainframe stuff IBM demos
#Main
spawn
ifstat ens33 >> /dev/null #This gets the stale history out of the way first
while ( true )
do	
	sleep 5s
	echo "$time seconds"
	system_metrics
	process_metrics
	time=$(($time+5))
done


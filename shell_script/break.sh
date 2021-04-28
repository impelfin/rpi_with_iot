#!/bin/bash
#break.sh
i=0
while [ $i -le 10 ]
do 
	let i+=1
	if [ $i -ge 3 ]
	then
		break
	fi
	echo $i
done


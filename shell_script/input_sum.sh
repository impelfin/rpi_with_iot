#!/bin/bash
echo -n "Input num : "
read x
i=0
sum=0
while [ $i -le $x ]
do
	let sum+=i
	let i+=1
done
echo 1~$x sum = $sum


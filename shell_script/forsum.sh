#!/bin/bash
echo -n "Input num : "
read x
sum=0
for ((i=0;i<=$x;i++)) 
do
	((sum+=i))
done
echo 1~$x sum = $sum


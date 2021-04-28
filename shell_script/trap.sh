#!/bin/bash
#trap.sh

trap 'echo "$LINENO : count=$count "' DEBUG

count=1
sum=0

while ((count<=10))
do
	((sum+=count))
	let count+=1
done

echo sum of 1~10 : $sum

#!/bin/bash
#until.sh

sum=0
i=0

until [ $i -gt 10 ]
do
	let "sum+=i"
	let "i+=1"
done
echo "The sum is $sum."

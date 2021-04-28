#!/bin/bash
#sign.sh

if [ $1 -gt 0 ]
then 
	echo "The number is $1 is positive."
elif [ $1 -eq 0 ]
then
	echo "The number $1 is zero."
else
	echo "The number $1 is negative."
fi

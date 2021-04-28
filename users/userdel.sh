#!/bin/bash

i=1

while [ $i -le 10 ]
do
	userdel -r user$i
	let i+=1
done
echo Complete!!

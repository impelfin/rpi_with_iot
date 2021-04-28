#!/bin/bash

i=1
uid=2000

while [ $i -le 10 ]
do
	let uid+=1
	useradd -u $uid -g users user$i
	passwd -d user$i
	let i+=1
done
echo Complete!!

#!/bin/bash

while [ $1 != "" ]
do
	useradd $1
	passwd -d $1
	shift
done
exit 0

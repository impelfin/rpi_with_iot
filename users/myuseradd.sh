#!/bin/bash

while read uname uid gid pw home
do
	echo "user $uname create."
	useradd -u $uid -g $gid -c $uname**$gid -d $home -p `./mycrypt $pw` $uname
done
echo
echo Complete!!

#!/bin/bash
#case2.sh

echo -e "Type y(yes) or n(no). : \c"
read input
case $input in 
	y | Y | yes) 
		echo "You selected yes.";;
	n | N | no) 
		echo "You selected no.";;
	*)
		echo "Please try again.";;
esac

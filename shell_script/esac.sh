#!/bin/bash
#easc.sh
echo -e "Type y(yes) or n(no). \c"
read input
case $input in
y | Y | yes)
	echo "your selected yes." ;;
n | N | no)
	echo "your selected no." ;;
*)
	echo "Please try again." ;;
esac


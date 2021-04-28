#!/bin/bash
#diff.sh

if [ $1 -ne $2 ]
then
	echo "The number $1 is different from $2."
fi
if [ $1 != $2 ]
then
	echo "The string $1 is different from $2."
fi

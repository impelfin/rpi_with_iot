#!/bin/bash

echo -n $0 : 
echo $$ 

if [ "$1" = ok ]; then
	echo "good~!!"
else
	echo "bad~!!"
fi


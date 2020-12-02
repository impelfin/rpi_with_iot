#!/bin/bash
#sum.sh
#set -xv

function sum {
	typeset sum

	((sum=$1+$2))
	return $sum
}

sum $1 $2
echo $1 + $2 = $?


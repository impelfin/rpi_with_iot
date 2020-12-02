#!/bin/bash
#local.sh

var=0
echo "global : var=$var."
func() {
	local var=1
	echo "func : var=$var."
	return 2
}
func $*
echo "global : return value=$?."
echo "global : var=$var."


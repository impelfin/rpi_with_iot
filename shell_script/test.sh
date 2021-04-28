#!/bin/bash
#test.sh

test 2 -eq 3
echo $?
test 2 -lt 3
echo $?
a=hong
test $a != "hong"
echo $?
[ -f test.sh ]
echo $?

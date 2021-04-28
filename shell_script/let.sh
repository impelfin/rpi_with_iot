#!/bin/bash
#let.sh
a=1
let "a+=5"
echo $a
b=$(($a+1))
echo $b
let "c=a & b"
echo $c
let "d=a>6 && b>6"
echo $d

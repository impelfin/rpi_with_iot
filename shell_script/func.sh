#!/bin/bash

func() {
	echo "func : $*"
	echo "func : argument number is $#"
}
func $*

#!/bin/bash
select file in $(ls e*)
do 
	echo "This file is $file"
done

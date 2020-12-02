#!/bin/bash
for ((i=1;i<=100;i++)) 
do
	if (($i%30 == 0 ))
	then
		echo -n " C "
		echo 
		continue;
	fi

	if (($i%3 == 0)) 
	then
		echo -n " C " 
		continue;
	elif (($i/10/10 == 3 || $i/10/10 == 6 || $i/10/10 ==9))
	then
		echo -n " C "
		continue;
	elif (($i/10%10 == 3 || $i/10%10 == 6 || $i/10%10 ==9))
	then
		echo -n " C "
		continue;
	elif (($i%10 == 3 || $i%10 == 6 || $i%10 ==9))
	then
		echo -n C
		continue;
	fi

	echo -n " $i "

	if (($i%10 == 0))
	then
		echo 
	fi
done


#!/bin/sh
count=0

for YEAR in $(seq 1902 2015);
do
 
	file="029500"
	DIR=/users/a/a/aametcal/wind/rawData/$YEAR/*

	if grep -r -q $file $DIR; then
		echo found
		let "count=count+1"
		echo $count
	else
		echo not foune $YEAR
	fi
done




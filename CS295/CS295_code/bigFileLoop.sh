#!/bin/sh
for YEAR in 2016 2017
do
	DIR=/users/a/a/aametcal/wind/$YEAR/*
	mkdir $YEAR
	for FILE in $DIR
	do
		java ishJava $FILE ~/CS295/$YEAR/`basename $FILE`'.txt'
		echo `basename $FILE`
	done
done 









#!/bin/sh
#DIR=/users/a/a/aametcal/wind/2000/*
#
#for FILE in $DIR
#do
#        echo `basename  $FILE`
#        java ishJava $FILE `basename  $FILE`'.txt'
#done

#!/bin/sh
DIR=/users/a/a/aametcal/wind/2000/*

for FILE in $DIR
do
	echo `basename  $FILE`
	java ishJava $FILE `basename  $FILE`'.txt'
done

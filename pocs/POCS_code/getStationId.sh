#!/bin/sh

WBAN=14914
Year=2015
Dir=/users/a/a/aametcal/wind/rawData/$Year/*

for file in $Dir
do
    if grep -q $WBAN $file
    then
        echo $file
    fi
done

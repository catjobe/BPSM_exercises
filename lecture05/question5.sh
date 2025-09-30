#!/bin/bash

unset IFS
IFS=$'\t'
count=0

while read name email city birthday_day birthday_month birthday_year country
do
	if [ "${birthday_month}" == "10" ]
	then
		if test "${country}" == "country"
		then
			echo "Skip"
		else
			count=$((count+1))
			echo "${country}:"
			echo "${name}"
			echo "TOTAL = ${count}"
			echo " "
			count=0	
		fi
	fi
done < example_people_data.tsv 

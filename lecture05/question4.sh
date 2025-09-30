#!/bin/bash

unset IFS
IFS=$'\t'
count=0

echo "Name Country"

while read name email city birthday_day birthday_month birthday_year country
do
	if [ "${birthday_month}" == "10" ]
	then
		count=$((count+1))
		echo "${name} ${country}"
	fi
done < example_people_data.tsv 

echo "TOTAL = ${count}"

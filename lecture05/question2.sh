#!/bin/bash

unset IFS
IFS=$'\t'
count=0

while read name email city birthday_day birthday_month birthday_year country
do
	if [ "${name}" = "name" ]
	then 
		continue
	fi
	count=$((count+1))
	echo -e "${count}\t${name}\t${city}\t${country}"
done < example_people_data.tsv | head -n -5

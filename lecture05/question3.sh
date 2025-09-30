#!/bin/bash

unset IFS
IFS=$'\t'
count=0

while read name email city birthday_day birthday_month birthday_year country
do
	if [ "${name}" == "name" ] || [ "${name}" == " " ]
	then
		continue
	fi
	if test ${country} == "country"
	then
		blah=blah
	else count=$((count+1))
		echo -e "${count}\t${name}\t${city}\t${country}" >> ${country// /}.out
	fi; done < example_people_data.tsv

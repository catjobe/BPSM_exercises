#!/bin/sh

myfavoritesequence="ACATAAAACATCAAAGTGAACAGATTGTAGTGTAAGAAGTTAGATTAA"

while read line
do read line2
	if [[ ${line2} == *${myfavoritesequence}* ]]
	then
		echo -e ${line}"\n"${line2}
	fi
done < $1

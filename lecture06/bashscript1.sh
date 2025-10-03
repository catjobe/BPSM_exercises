#!/bin/bash

unset IFS
IFS=$'\t'

rm *.output

input_file="blastoutput2.out"
hsp_count=0
length_count=0
line_number=0
dups=0
all_array=()
duplicate_array=()

while read line
do
	if test ${line:0:1} != "#"
	then 
		read query subject per_identity align_length mismatch gaps qstart qend sstart send evalue bitscore <<< ${line}
		bitscore=$(printf "%.0f\n" ${bitscore})
		line_number=$((line_number+1))
		
		# Question 1
		echo "${subject}" >> question1_subjectaccession.output

		# Question 2
		echo -e "${align_length}\t${per_identity}" >> question2.output

		# Question 3
		if test ${mismatch} -gt 20
		then
			echo "${line}" >> question3.output
		fi

		# Question 4
		if test ${align_length} -lt 100 && test ${mismatch} -gt 20
		then
			echo "${line}" >> question4.output
		fi

		# Question 5
		if test ${mismatch} -lt 20
		then
			hsp_count=$((hsp_count+1))
			if test ${hsp_count} -le 20
			then
				echo "${line}" >> question5.output
			fi
		fi

		# Question 6
		if test ${align_length} -lt 100
		then
			length_count=$((length_count+1))
		fi

		# Question 7
		if test ${line_number} -le 10
		then
			echo "${line}" >> question7.output
		fi

		# Question 8
		if [[ ${subject} == *"AEI"* ]]
		then
			echo "${subject} starts at subject ${sstart}, query ${qstart}" >> question8.output
		fi

		# Question 9
		acc=$(echo "${subject}" | cut -d"|" -f4)
		if [[ "${all_array[@]}" =~ "${acc}" ]]
		then
			match=match
			if [[ ! "${duplicate_array[@]}" =~ "${acc}" ]]
			then
				dups=$((dups+1))
				duplicate_array+=("${acc}")
			fi
		else
			all_array+=("${acc}")
		fi
		
		# Question 10
		percent_mismatch=$((100*${mismatch}/${align_length}))
		echo -e "${line}\t${percent_mismatch}" >> question10.output

		# Question 11
		if test ${bitscore} -lt 187
		then
			echo ${line} >> question11_lowbitscore.output
		else
			echo ${line} >> question11_highbitscore.output
		fi

	fi
done < ${input_file}

echo "There are ${length_count} HSPs shorter than 100 amino acids"
echo "There are ${dups} subject sequences that have more than one HSP"

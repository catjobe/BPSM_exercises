#!/bin/bash

rm singleline_NCBIseq_bash.fasta

count=0
while read line
do 
	[ -z "${line}" ] && continue
	if test ${line:0:1} == ">"
	then
		count=$(( ${count}+1 ))
		if test ${count} == 1
		then
			printf ${line}"\n" >> singleline_NCBIseq_bash.fasta
		else
			printf "\n"${line}"\n" >> singleline_NCBIseq_bash.fasta
		fi
	else
		printf ${line} >> singleline_NCBIseq_bash.fasta
	fi
done < mock_NCBI.fasta 

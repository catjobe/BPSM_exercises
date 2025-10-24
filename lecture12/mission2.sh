#!/bin/bash

for file in *.fa 
do
	echo ${file}
	blastx -db nem -query ${file} -outfmt 7 | grep -v "^#" | head -1
done

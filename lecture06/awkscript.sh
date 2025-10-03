#!/bin/bash

input_file="blastoutput2.out"

# Question 1
echo "Subject Accessions"
grep -v "^#" ${input_file} | cut -f2
echo " "

# Question 2
echo "Percent Identity, Alignment Length"
grep -v "^#" ${input_file} | cut -f4,3
echo " "

# Question 3
echo "query acc.ver, subject acc.ver, % identity, alignment length, mismatches, gap opens, q. start, q. end, s. start, s. end, evalue, bit score"
grep -v "^#" ${input_file} | awk '{if ($5 > 20){print $0;}}'
echo " "

# Question 4
echo "query acc.ver, subject acc.ver, % identity, alignment length, mismatches, gap opens, q. start, q. end, s. start, s. end, evalue, bit score"
grep -v "^#" ${input_file} | awk '{if ($5 > 20 && $4 < 100){print $0;}}'
echo " "

# Question 5
echo "query acc.ver, subject acc.ver, % identity, alignment length, mismatches, gap opens, q. start, q. end, s. start, s. end, evalue, bit score"
grep -v "^#" ${input_file} | awk '{if ($5 < 20){print $0;}}' | head -n20
echo " "

# Question 6
aa_100=$(grep -v "^#" ${input_file} | awk '{if ($4 < 100){print $0;}}' | wc -l)
echo "There are ${aa_100} HSPs are shorter than 100 amino acids"
echo " "

# Question 7
echo "query acc.ver, subject acc.ver, bit score"
grep -v "^#" ${input_file} | cut -f1,2,12 | sort -k3 -nr | head -10
echo " "

# Question 8
echo "Accession, Start Position"
cut -f2,7 ${input_file} | grep "AEI"
echo " "

# Question 9
subseq=$(grep -v "^#" ${input_file} | cut -f2 | cut -d "|" -f4 | sort | uniq -c | sort -k1 -n | awk '{if ($1>1) {print $0;}}' | wc -l)
echo "${subseq} subject sequences have more than one HSP"
echo " "

# Question 10
echo "query acc.ver, subject acc.ver, % identity, alignment length, mismatches, gap opens, q. start, q. end, s. start, s. end, evalue, bit score, % mismatch"
grep -v "^#" ${input_file} | awk '{OFS="\t";}{if ($5!=0){print $0, $5/$4*100;}}'
echo " "

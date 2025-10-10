#!/bin/bash
#$ -cwd -V
#$ -t 1-100
#$ -N ArrayJob

splitdir=${HOME}"/testing_eddie/split_reads_directory"

./myanalysis.sh ${splitdir}/reads-${SGE_TASK_ID}

#$ -o results.output
#$ -e results.error

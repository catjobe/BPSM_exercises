#!/usr/bin/python3

import sys

# Command Line Arguments
dna = sys.argv[1]
k = int(sys.argv[2])
n = int(sys.argv[3])

# Initialize an empty list
kmer_list = []
uniq_kmer = []

# Add each kmer into the list
for i in range(0,len(dna)-k+1):
    kmer = dna[i:i+k]
    kmer_list.append(kmer)

# Find all kmers that are present more than n times, and append only unique copies of that kmer to a new list
for kmer in kmer_list:
    if kmer_list.count(kmer) > n and kmer not in uniq_kmer:
        uniq_kmer.append(kmer)

# Print unique kmers
for kmer in uniq_kmer:
    print(kmer)

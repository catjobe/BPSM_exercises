#!/usr/bin/python3

import sys

# Get command line arguments
dna_seq = sys.argv[1]
kmer = int(sys.argv[2])
n = int(sys.argv[3])

# Function that prints list of kmers that occur more than a certain number of times for a given DNA sequence
def kmer_counter(dna_seq,kmer,n):
    kmer_list=[]
    for i in range(0,len(dna_seq)-kmer+1):
        kmer_t=dna_seq[i:i+kmer]
        kmer_list.append(kmer_t)
    uniq_kmer=list(set(kmer_list))
    kmers_to_return=[]
    for kmer_d in uniq_kmer:
        if kmer_list.count(kmer_d) > n:
            kmers_to_return.append(kmer_d)
    return kmers_to_return
        

# Testing the function
print(kmer_counter(dna_seq,kmer,n))

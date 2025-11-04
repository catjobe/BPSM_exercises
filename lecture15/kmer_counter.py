#!/usr/bin/python3

def kmer_counter(dna_seq,n):
    kmers=list(range(2,len(dna_seq)-1))
    all_kmers=[]
    for kmer in kmers:
        kmer_list=[]
        for i in range(0,len(dna_seq)-kmer+1):
            kmer_t=dna_seq[i:i+kmer]
            kmer_list.append(kmer_t)
        uniq_kmer=list(set(kmer_list))
        kmers_to_return=[]
        for kmer_d in uniq_kmer:
            if kmer_list.count(kmer_d) > n:
                kmers_to_return.append(kmer_d)
        all_kmers+=kmers_to_return
    return all_kmers
        

# Testing the function
print(kmer_counter("AAAAAAAAAAATATATATATTTTAAA",2))

#!/usr/bin/python3

# Length of DNA sequences of the same length
dna_seqs = ['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']

for seq1 in dna_seqs:
    for seq2 in dna_seqs:

        # I first want to avoid comparing the same sequences to each other
        if seq1 != seq2:

            # Initalize a counter for the comparison of each pair of sequences
            count=0

            # Comparing the identity of bases at each position for a pair of sequences
            for base in range(0, len(seq1)):
                if seq1[base] == seq2[base]:
                    count+=1

            print(seq1, seq2, count, count/len(seq1))

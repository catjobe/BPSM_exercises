#!/usr/bin/python3

dna_seq='ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'
a_count=dna_seq.count('A')
t_count=dna_seq.count('T')
at_count=a_count+t_count
total_length=len(dna_seq)

print('AT countent is:', at_count/total_length)

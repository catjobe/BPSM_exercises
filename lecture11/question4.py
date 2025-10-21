#!/usr/bin/python3

dna_seq='ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT'

# Define start and stop positions for each exon
exon1_start=0
exon1_end=63+2
exon2_start=91+1

# Find exons
exon1=dna_seq[exon1_start:exon1_end]
exon2=dna_seq[exon2_start:]

# Make CDS
cds=exon1+exon2

# Calculate percentage of DNA sequence that is coding
perc_cds=len(cds)/len(dna_seq)*100
print('The precentage of DNA sequence that is coding is:', perc_cds)

# Prints the original genomic DNA sequence with coding bases in uppercase, non-coding bases in lowercase
intron=dna_seq[exon1_end+1:exon2_start-1]
dna_seq_ie=exon1+intron.lower()+exon2
print(dna_seq_ie)

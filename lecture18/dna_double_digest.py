#!/bin/usr/python3

import re

infile = open('/localdisk/data/BPSM/Lecture18/long_dna.txt')
dna = infile.read().rstrip()

# Single digest
print('Single Digest')

bpsmI_match=list(re.finditer(r'A[GCAT]TAAT',dna))

single_dig={}

# Extract cut sites
all_cuts=[]
counter=0
for dig in bpsmI_match:
        all_cuts.append(bpsmI_match[counter].start()+3)
        counter+=1

# Calculating fragment length and identifying sequence
cut_length=0
for cut in all_cuts:
    frag_length=cut-cut_length
    single_dig[frag_length]=dna[cut_length:cut-1]
    cut_length+=frag_length
single_dig[len(dna)-cut_length]=dna[cut_length:]
print(single_dig)


# Double digest
print('\n\nDouble Digest')
bpsmII_match=list(re.finditer(r'GC[AG][AT]TG',dna))

double_dig={}

# Extract cut sites
counter=0
for dig in bpsmII_match:
        all_cuts.append(bpsmII_match[counter].start()+4)
        counter+=1

all_cuts.sort()

# Calculating fragment length and identifying sequence
cut_length=0
for cut in all_cuts:
    frag_length=cut-cut_length
    double_dig[frag_length]=dna[cut_length:cut-1]
    cut_length+=frag_length
double_dig[len(dna)-cut_length]=dna[cut_length:]
print(double_dig)

infile.close()

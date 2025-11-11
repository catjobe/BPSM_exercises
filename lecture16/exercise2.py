#!/bin/bash

# Asks the user to input a DNA sequence
dna = input('Provide a DNA Sequence ')

# Remove undetermined bases or any inappropriate values in input
for base in dna:
    if base not in ['A','C','T','G']:
        dna = dna.replace(base,'')

# Generates reverse
dna_rev = dna[::-1].replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()

# Codon Table
gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

# Loop that will generate all translations
for seq in dna, dna_rev:
    if seq == dna:
        strand='Forward'
    else:
        strand='Reverse'
    for i in range(0,3):
        protein=[]
        for j in range(i,len(seq)-3+1,3):
            nucleotide=seq[j:j+3]
            aa=gencode[nucleotide]
            protein.append(aa)
        print(strand, seq, '\nFrame:', str(i+1), '\n', ''.join(protein),'\n')

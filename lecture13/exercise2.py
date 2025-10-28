#!/usr/bin/python3

# Read the necessary data
gen_in=open("genomic_dna2.txt")
gen_data=gen_in.read()
exon_in=open("exons.txt")
exons=exon_in.readlines()

# Initalize a list that will contain all the exon fragments
exon_segments=[]

# Extract exons
for exon in exons:
    start=int(exon.rstrip().split(',')[0])
    end=int(exon.rstrip().split(',')[1])
    exon_segments.append(gen_data.rstrip('\n')[start:end+1])

# Write the output to a new file
outfile=open("exon_output.txt", "w")
outfile.write(''.join(exon_segments))
outfile.close() 

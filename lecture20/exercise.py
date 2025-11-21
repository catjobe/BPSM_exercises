#!/bin/usr/python3

from Bio import SeqIO
from Bio import Entrez

# Search
myresult_mammal=Entrez.read(Entrez.esearch(db="protein", term="mammalia COX1 complete",retmax='1000'))

# Question 1: The number of complete COX1 protein records for mammals
print("There are", myresult_mammal['Count'], "complete COX1 protein records for mammals")

# Question 2: Average Length

# Initialize variables for calculating mean
counter=0
lengths=0

# Loop to fetch individual proteins
for accession in myresult_mammal['IdList']:
    counter+=1
    genbank=Entrez.efetch(db="protein",id=accession,rettype="gb")
    record=SeqIO.read(genbank,"genbank")
    lengths+=len(record.seq)
    print(record.description)

print("There are", counter, "complete COX1 protein records for mammals")

# Calculating mean protein length
mean_length=lengths/counter

print("The average length of the protein is:", mean_length)

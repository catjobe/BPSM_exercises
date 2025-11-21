#!/bin/usr/python3

from Bio import SeqIO
from Bio import Entrez

# Take user inputs
gene=input("Enter gene name: ")
taxon=input("Enter taxonomic group: ")

while True:
    try:
        retmax=int(input("Enter the maximum number of return results: "))
        break
    except:
        "Please provide a valid integer value! Try again!"


# Function to conduct the protein search, and desired analyses
def protein_search(gene_name, taxonomic_group, retmax_val):

    # Generate the search term
    search_term="complete " + taxonomic_group + " " + gene_name

    # Conduct the search
    myresult=Entrez.read(Entrez.esearch(db="protein", term=search_term, retmax=retmax_val))

    # Initialize variables
    counter=0
    lengths=0

    # Access entry for each protein to calculate average protein length
    for accession in myresult['IdList']:
        counter+=1
        genbank=Entrez.efetch(db="protein",id=accession,rettype="gb")
        record=SeqIO.read(genbank,"genbank")
        lengths+=len(record.seq)
    
    # Create output strings
    q1 = "There are "+str(counter)+ " complete " + gene_name + " protein records for " + taxonomic_group

    mean_length=int(lengths/counter)

    q2 = "The average length of the protein is: " + str(mean_length)
    
    answers = q1+"\n"+q2

    return answers

# Run the function based on user inputs:
print(protein_search(gene, taxon, retmax))    

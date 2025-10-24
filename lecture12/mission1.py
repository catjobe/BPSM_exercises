#!/usr/bin/python3

import subprocess

# Read the data

infile = open("plain_genomic_seq.txt")
gene_seq = infile.read()

# Clean the data

gene_seq_clean = gene_seq.replace("X","").replace("\n","").replace("K","").replace("L","").upper()

# Extracting the sequences

plain_exon1=gene_seq_clean[:63]
plain_exon2=gene_seq_clean[90:]
plain_intron=gene_seq_clean[63:90] 

# Creating the headers

header1 = ">plain_exon1:"+str(len(plain_exon1))
header2 = ">plain_exon2:"+str(len(plain_exon2))
header3 = ">plain_intron:"+str(len(plain_intron))

# Write the output to files

outfile1 = open("plain_exon1.fa", "w")
outfile1.write(">plain_exon1:"+str(len(plain_exon1))+"\n"+gene_seq_clean[:63])
outfile1.close()

outfile2 = open("plain_exon2.fa", "w")
outfile2.write(">plain_exon2:"+str(len(plain_exon2))+"\n"+gene_seq_clean[90:])
outfile2.close()

outfile3 = open("plain_intron.fa", "w")
outfile3.write(">plain_intron:"+str(len(plain_intron))+"\n"+gene_seq_clean[63:90])
outfile3.close()

outfile_exons = open("plain_exons.fa", "w")
outfile_exons.write(">plain_exon1:"+str(len(plain_exon1))+"\n"+gene_seq_clean[:63]+"\n")
outfile_exons.write(">plain_exon2:"+str(len(plain_exon2))+"\n"+gene_seq_clean[90:])
outfile_exons.close()

outfile_introns = open("plain_introns.fa", "w")
outfile_introns.write(">plain_intron:"+str(len(plain_intron))+"\n"+gene_seq_clean[63:90])
outfile_introns.close()

infile.close()

# Access the remote files

subprocess.call('wget -qO AJ223353.fa "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AJ223353&rettype=fasta&retmode=text"', shell=True) 
subprocess.call('wget -qO AJ223353.annot "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AJ223353&rettype=genbank&retmode=text"', shell=True)

# Read the data

infile = open("AJ223353.fa")
remote_gene_seq = infile.read()

remote_gene_seq_clean = remote_gene_seq.rstrip().replace(">AJ223353.1 Homo sapiens mRNA for histone H2B, clone pJG4-5-15","").replace("\n","")

# Process the annotation file to find the necessary start and end indices

start = int(subprocess.check_output('grep "CDS" AJ223353.annot | awk \'{FS="\t";}{print $2;}\'', shell=True).decode("utf-8").rstrip().split("..")[0]) 
end = int(subprocess.check_output('grep "CDS" AJ223353.annot | awk \'{FS="\t";}{print $2;}\'', shell=True).decode("utf-8").rstrip().split("..")[1])

# Extracting the sequences

remote_noncds1 = remote_gene_seq_clean[:start]
remote_noncds2 = remote_gene_seq_clean[end+1:]
remote_cds = remote_gene_seq_clean[start+1:end+1] 

# Write the output to files

outfile1 = open("remote_noncds1.fa", "w")
outfile1.write(">remote_noncds1:"+str(len(remote_noncds1))+"\n"+remote_gene_seq_clean[:start])
outfile1.close()

outfile2 = open("remote_noncds2.fa", "w")
outfile2.write(">remote_noncds2:"+str(len(remote_noncds2))+"\n"+remote_gene_seq_clean[end+1:])
outfile2.close()

outfile3 = open("remote_cds.fa", "w")
outfile3.write(">remote_cds:"+str(len(remote_cds))+"\n"+remote_gene_seq_clean[start+1:end+1])
outfile3.close()

outfile_exons = open("remote_noncds.fa", "w")
outfile_exons.write(">remote_noncds1:"+str(len(remote_noncds1))+"\n"+remote_gene_seq_clean[:start]+"\n")
outfile_exons.write(">remote_noncds2:"+str(len(remote_noncds2))+"\n"+remote_gene_seq_clean[end+1:])
outfile_exons.close()

outfile_introns = open("remote_cds.fa", "w")
outfile_introns.write(">remote_cds:"+str(len(remote_cds))+"\n"+remote_gene_seq_clean[start+1:end+1])
outfile_introns.close()

infile.close()

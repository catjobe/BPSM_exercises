#!/usr/bin/python3

# Open the data file
infile=open("remote_cds.fa")
cds=infile.readlines()

# Extract the sequence itself
cds_seq=cds[1] 

# Part 1: Prints sliding window to the screen

for sw in range(0,len(cds_seq)-29,3):
    print(cds_seq[sw:sw+30]) 

# Part 2: Prints GC content of each sliding window segment to the screen

for sw in range(0,len(cds_seq)-29,3):
    g=cds_seq[sw:sw+30].count('G')
    c=cds_seq[sw:sw+30].count('C')
    gc=(g+c)/30
    print("GC content for", cds_seq[sw:sw+30], "is", gc) 

# Part 3: Writes each individual segment in fasta format to individual fasta files

for sw in range(0,len(cds_seq)-29,3):
    filename='fasta'+str(int(sw/3))+'.fasta'
    outfile=open(filename, 'w')
    header='>sequence'+str(int(sw/3))+'\n'
    line=cds_seq[sw:sw+30]+'\n'
    outfile.write(header)
    outfile.write(line)
    outfile.close() 

# Part 4: Writes each individual segment in fasta format to one fasta file

outfile=open('allfasta.fasta', 'w')

for sw in range(0,len(cds_seq)-29,3):
    header='>sequence'+str(int(sw/3))+'\n'
    line=cds_seq[sw:sw+30]+'\n'
    outfile.write(header)
    outfile.write(line)

outfile.close() 

# Part 5: Includes partial sliding window segments

for sw in range(0,len(cds_seq),3):
    print(cds_seq[sw:sw+30])

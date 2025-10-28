#!/usr/bin/python3

import subprocess
import os

# Open the file
infile=open("xaa.dna")

# Process the lines
sequences=infile.readlines()

# Initialize a counter
count=0

# This for loop generates the files and directories associated with sequences of certain lengths, and moves the corresponding files to the directory
for seq in sequences:
    count+=1
    seq_len=len(seq.rstrip('\n'))
    filename="sequence"+str(count)+".txt"
    with open(filename, "w") as outfile:
        outfile.write(seq)
    for nums in range(9):
        start=(nums+1)*100
        end=start+99
        if start <= seq_len <= end:
            directory_name="bp"+str(start)+"_"+str(end)
            os.makedirs(directory_name, exist_ok=True)
            subprocess.call(f"mv sequence{count}.txt bp{start}_{end}/sequence{count}.txt", shell=True)
            break

infile.close()

#!/usr/bin/python3

# Checking for the percent of undetermined bases in inputted DNA sequence
def undetermined_bases(dna_seq, threshold=0.1):
    seq_length=len(dna_seq)
    base_count=0
    for base in dna_seq:
        if base.lower() not in 'a' 'c' 't' 'g':
            base_count+=1
    undetermined_base=base_count/seq_length
    if undetermined_base >= threshold:
        return "True"
    else:
        return "False"

# Testing the function
print(undetermined_bases("ACTNNN")) # True
print(undetermined_bases("ACTGGG")) # False
print(undetermined_bases("ACTNNN", threshold=0.6))
print(undetermined_bases("ACTNEFN", threshold=0.6))

assert undetermined_bases("ACTNNN") == "True"
assert undetermined_bases("ACTGGG") == "False"
assert undetermined_bases("ACTNEFNNNN", threshold=0.6) == "True"

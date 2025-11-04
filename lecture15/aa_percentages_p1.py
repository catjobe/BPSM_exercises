#!/usr/bin/python3

# Function that returns percentage of protein that a given amino acid makes up
def aa_percent(prot_seq, aa):
    prot_length = len(prot_seq)
    aa_count = prot_seq.count(aa)
    aa_percent = (aa_count/prot_length)*100
    return aa_percent

# Testing function
print(aa_percent("MSRSLLLRFLLFLLLLPPLP", "M"))
assert round(aa_percent("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)

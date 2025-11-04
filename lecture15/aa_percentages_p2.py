#!/usr/bin/python3

# Function that accepts a list of amino acid residues
def aa_percent(prot_seq, aa=['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']):
    prot_length = len(prot_seq)
    tot_aa_count = 0
    for a in aa:
        aa_count = prot_seq.count(a)
        tot_aa_count+=aa_count
    aa_percent = (tot_aa_count/prot_length)*100
    return aa_percent

# Testing with assertions
print(round(aa_percent("MSRSLLLRFLLFLLLLPPLP", ["M"]),5))
print(aa_percent("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']))
print(aa_percent("MSRSLLLRFLLFLLLLPPLP"))
assert round(aa_percent("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5
assert round(aa_percent("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])) == 70
assert round(aa_percent("MSRSLLLRFLLFLLLLPPLP")) == 65

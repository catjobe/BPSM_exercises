#!/usr/bin/python3

dna_seq='ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT'

eco_ri='GAATTC'

# Find the cut position
cut_pos=dna_seq.find(eco_ri)+1

# Calculate the length of the second fragment
first_frag=cut_pos
sec_frag=len(dna_seq)-cut_pos

print('The length of the first fragment is:', first_frag, '\n' + 'The length of the second fragment is:', sec_frag)

#!/usr/bin/python3

# Open the file
input_data=open("input.txt") 

# Extract each line and put it into a list
in_data=input_data.readlines() 

out_data=open("output_cleaned.txt", "w")

# Remove the sequencing adaptor sequence
for sequence in in_data:
    out_data.write(sequence[15:])
    print(len(sequence[15:].rstrip('\n')))

out_data.close()


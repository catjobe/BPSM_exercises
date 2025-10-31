#!/usr/bin/python3

# Import the file
infile=open('data.csv')
d_mel=infile.readlines() 

# Part 1

print('Part 1')

for fly in d_mel:

    # Process each object
    fields=fly.rstrip().split(',')

    # Assign each element to what they are
    species_name=fields[0]
    sequence=fields[1]
    gene_name=fields[2]
    expression_level=fields[3]

    gene_length=len(sequence)

    a_count=sequence.count('a')
    t_count=sequence.count('t')

    if species_name == 'Drosophila melanogaster' or species_name == 'Drosophila simulans':
        print(species_name, gene_name)

# Part 2

print('\nPart 2')

for fly in d_mel:

    fields=fly.rstrip().split(',')

    species_name=fields[0]
    sequence=fields[1]
    gene_name=fields[2]
    expression_level=fields[3]

    gene_length=len(sequence)
    if gene_length >= 90 and gene_length <= 100:
        print(gene_name, gene_length)

# Part 3

print('\nPart 3')

for fly in d_mel:

    fields=fly.rstrip().split(',')
    
    species_name=fields[0]
    sequence=fields[1]
    gene_name=fields[2]
    expression_level=fields[3]

    a_count=sequence.count('a')
    t_count=sequence.count('t')

    at_count=a_count+t_count
    at_content=at_count/gene_length

    if at_content > 0.5 and int(expression_level) > 200:
        print(gene_name, at_content, expression_level)

# Part 4

print('\nPart 4')

for fly in d_mel:

    fields=fly.rstrip().split(',')

    species_name=fields[0]
    sequence=fields[1]
    gene_name=fields[2]
    expression_level=fields[3]

    if (gene_name[0] == 'k' or gene_name[0] == 'h') and species_name != 'Drosophila melanogaster':
        print(gene_name)

# Part 5

print('\nPart 5')
print('Gene Name', 'AT > 0.65', 'AT < 0.45', '0.45 < AT < 0.65')

for fly in d_mel:

    fields=fly.rstrip().split(',')
    
    species_name=fields[0]
    sequence=fields[1]
    gene_name=fields[2]
    expression_level=fields[3]
    
    a_count=sequence.count('a')
    t_count=sequence.count('t')
    
    at_count=a_count+t_count
    at_content=at_count/gene_length

    if at_count > 0.65:
        print(gene_name, 'High AT content')
    elif at_count < 0.45:
        print(gene_name, 'Low AT content')
    else:
        print(gene_name, 'Medium AT content')

infile.close()

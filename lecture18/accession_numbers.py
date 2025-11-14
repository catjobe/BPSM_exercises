#!/bin/usr/python3

import re

# List of gene accession numbers
accs = ['xkn59438','yhdck2','eihd39d9','chdsye847','hedle3455','xjhd53e','45da','de37dp']

# 1: Accession number contains the number 5
print('Accessions that contain the number 5:')

for acc in accs:
    if re.search('5',acc):
        print(acc)

# 2: Accession number contains the letter d or e
print('\nAccessions that contain the letter d or e:')
for acc in accs:
    if re.search('(d|e)',acc):
        print(acc)

# 3: Accession number contains the letter d and e in that order
print('\nAccessions that contain the letter d and e, in that order:')

for acc in accs:
    if re.search('de',acc):
        print(acc)

# 4: Accession number contains the letter d and e in that order with single letter between them
print('\nAccessions that contain the letter d and e, in that order, with single letter between then:')

for acc in accs:
    if re.search('d.e',acc):
        print(acc)

# 5: Accession number contains d and e in any order
print('\nAccessions that contains d and e in any order')

for acc in accs:
    if re.search(r'(e\w*d|d\w*e)',acc):
        print(acc)

# 6: Accession number that starts with x or y
print('\nAccessions that starts with x or y')

for acc in accs:
    if re.search(r'(^x|^y)', acc):
        print(acc)

# 7: Accession number that starts with x or y and ends with e
print('\nAccessions that starts with x or y and ends with e')

for acc in accs:
    if re.search(r'(^x|^y)', acc) and re.search(r'e$', acc):
        print(acc)

# 8: Accession number that contains any 3 numbers in any order
print('\nAccessions that contain any 3 numbers in any order')

for acc in accs:
    if re.search(r'(\D*\d\D*\d\D*\d\D*)',acc) and (len(re.findall(r'\d', acc)) == 3):
        print(acc)

# 9: Accession number that contains 3 different numbers in the accession
print('\nAccessions that contain 3 different numbers in the accession')

for acc in accs:
    if (len(re.findall(r'\d', acc)) == 3):
        if re.search(r'\D*(\d)\D*(\d)\D*(\d)\D*',acc).group(1) != re.search(r'\D*(\d)\D*(\d)\D*(\d)\D*',acc).group(2) and re.search(r'\D*(\d)\D*(\d)\D*(\d)\D*',acc).group(1) != re.search(r'\D*(\d)\D*(\d)\D*(\d)\D*',acc).group(3) and re.search(r'\D*(\d)\D*(\d)\D*(\d)\D*',acc).group(2) != re.search(r'\D*(\d)\D*(\d)\D*(\d)\D*',acc).group(3):
            print(acc)

# 10: Accesssion number that contains 3 or more numbers in a row
print('\nAccesssions that contains 3 or more numbers in a row')

for acc in accs:
    if re.search(r'\d{3,}',acc):
        print(acc)

# 11: Accession number that ends with d followed by either a,r,p
print('\nAccessions that ends with d followed by either a,r,p')

for acc in accs:
    if re.search(r'(d[rop]$)',acc):
        print(acc)

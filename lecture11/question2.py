#!/usr/bin/python3

dnaseq='ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'

dnaseq1=dnaseq.replace('A','t')
dnaseq2=dnaseq1.replace('T','a')
dnaseq3=dnaseq2.replace('G','c')
dnaseq4=dnaseq3.replace('C','g')

print('Original sequence: ' + dnaseq + '\n' + 'Complement: ' + dnaseq4.upper())

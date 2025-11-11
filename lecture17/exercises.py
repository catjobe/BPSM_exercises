#!/bin/usr/python3

import os,sys,subprocess
import numpy as np
import pandas as pd

# Reading the data file
df = pd.read_csv('eukaryotes.txt',sep='\t',na_values=['-'])

# Question 1
print("Question 1")

print(df[df.apply(lambda x: x['Group'] in ['Fungi'] and x['Size (Mb)'] > 100,axis=1)].shape[0])

names=list(df[df.apply(lambda x: x['Group'] in ['Fungi'] and x['Size (Mb)'] > 100,axis=1)]['#Organism/Name']) 

for name in names:
    print(name)

# Question 2
print("\n\nQuestion 2")

print(df.loc[df['Group'] != "Other"]['Group'].value_counts())

# Question 3
print("\n\nQuestion 3")

df['genus']=df.apply(lambda x: x['#Organism/Name'].split(' ')[0], axis=1)
helic = df.loc[df['genus'] == "Heliconius"]
helic2 = helic.loc[helic['Status'] != "Scaffold"]
print(helic2[['#Organism/Name']])

# Question 4
print("\n\nQuestion 4")

print("\nPlants")
print(df[df.apply(lambda x: x['Group'] == 'Plants', axis=1)]['Center'].value_counts().head(1))

print("\nInsects")
print(df[df.apply(lambda x: x['SubGroup'] == 'Insects', axis=1)]['Center'].value_counts().head(1))

# Question 5
print("\n\nQuestion 5")

df['ProtPerGene'] = df['Proteins']/df['Genes']
print(df.loc[df['ProtPerGene'] >= 1.1][['#Organism/Name','ProtPerGene']])

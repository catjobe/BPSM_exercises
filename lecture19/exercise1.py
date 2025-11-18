#!/bin/usr/python3

import os,sys,subprocess
import numpy as np
import matplotlib.pyplot as plt

# Open the file
ecoli=open('/localdisk/data/BPSM/Lecture19/ecoli.txt').read().replace('\n','').lower()

# For entire genome
window=1000

at=[]

for wind in range(0,len(ecoli)-window):
    start=wind
    end=wind+window
    win_seq=ecoli[start:end]
    a_count=win_seq.count('a')
    t_count=win_seq.count('t')
    at.append((a_count+t_count)/window)

plt.figure(figsize=(20,10))
plt.plot(at,label='AT')
plt.ylabel('Fraction of bases')
plt.xlabel('Location')
plt.legend()
plt.savefig('ecoli_genome.png',transparent=True)

# Function
def plot_at_composition(sequence,size):
    window=1000
    seq=sequence[0:size]
    at=[]

    for wind in range(0,len(seq)-window):
        start=wind
        end=wind+window
        win_seq=seq[start:end]
        a_count=win_seq.count('a')
        t_count=win_seq.count('t')
        at.append((a_count+t_count)/window)

    plt.figure(figsize=(20,10))
    plt.plot(at,label='AT')
    plt.ylabel('Fraction of bases')
    plt.xlabel('Location')
    plt.legend()

    file_name="ecoli"+str(size)+".png"

    plt.savefig(file_name,transparent=True)

# For the first 50000 bases
plot_at_composition(ecoli,50000)

# For the first 100000 bases
plot_at_composition(ecoli,100000)

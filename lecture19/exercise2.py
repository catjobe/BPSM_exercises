#!/bin/usr/python3

import os,sys,subprocess
import numpy as np
import matplotlib.pyplot as plt

# Open the file
ecoli=open('/localdisk/data/BPSM/Lecture19/ecoli.txt').read().replace('\n','').lower()

# Get user inputs and check they are in a proper format
while True:
    try:
        window=int(input('Window Size? '))
        break
    except:
        print('Please try again with an integer')

while True:
    at_gc=input('AT or GC? ')
    if at_gc.lower() == 'at' or at_gc.lower() == 'gc':
        break
    else:
        print('Not GC or AT - Please try again')


while True:
    try:
        base_range=int(input('Provide numerical base range: '))
        break
    except:
        print('Please try again with an integer')

# Function for generating the plot with user inputs
def plot_at_composition(sequence,size,window,gc_at):
    
    seq=sequence[0:size]
    content=[]
    
    # Base content calculations
    for wind in range(0,len(seq)-window):
        start=wind
        end=wind+window
        win_seq=seq[start:end]
        if gc_at.lower() == 'at':
            a_count=win_seq.count('a')
            t_count=win_seq.count('t')
            content.append((a_count+t_count)/window)
            plot_label="AT"
        else:
            g_count=win_seq.count('g')
            c_count=win_seq.count('c')
            content.append((g_count+c_count)/window)
            plot_label="GC"
    
    # Create plot
    plt.figure(figsize=(20,10))
    plt.plot(content,label=plot_label)
    plt.ylabel('Fraction of bases')
    plt.xlabel('Location')
    plt.title('Base Composition Plot')
    plt.legend()
    
    file_name="ecoli"+"_"+str(size)+"_"+gc_at+".png"

    plt.savefig(file_name,transparent=True)

# Creating the plot with user inputs
plot_at_composition(ecoli,base_range,window,at_gc)

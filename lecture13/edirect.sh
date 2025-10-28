#!/bin/bash

# Question 1

ls -a ~/edirect/

# Question 2

ls -a ~/edirect/ | grep -v "^d" | egrep "^e|^x" | wc -l

# Question 3

ls -al ~/edirect/ | grep "^d" | egrep "^e|^x" | wc -l 

#!/bin/bash

# Function that will return a comment for each input
def comments_to_return(answer):
    answers=[]
    for key in answer:
        ans='You said your ' + str(key) + ' was ' + str(answer[key])
        answers.append(ans)
    for r in answers:
        print(r)

# Creating an empty dictionary to contain the responses
response={}

# Asking for input from the user, and checking that they provided valid inputs
response['name'] = input('What is your name? ')

while True:
    age = input('What is your age? ')
    try:
        if int(age) >= 0:
            response['age'] = age
            break
        else:
            print("I didn't understand that, please try again!")
    except:
        print("I didn't understand that, please try again!")

response['color'] = input('What is your favorite color? ')

while True:
    py_pref = input('Do you like Python (yes/no)? ')
    if py_pref.lower() == 'yes' or py_pref.lower() == 'no':
        response['py_pref'] = py_pref
        break
    else:
        print("I didn't understand that, please try again!")

while True:
    flat_world = input('The world is flat: True or False? ')
    if flat_world.lower() == "true" or flat_world.lower() == "false":
        response['flat_world'] = flat_world
        break
    else:
        print("I didn't understand that, please try again!")
    

comments_to_return(response)

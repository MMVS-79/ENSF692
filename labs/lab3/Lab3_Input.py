#! /usr/bin/env python3
# ENSF 692 Spring 2025
# May 13 Lab 3
# Exercise 3 - Solutions

# Add comments to explain the functionality of this program

# Input Method 1
print('\n') # prints new line
print("***METHOD 1***")  # prints method name
input1 = input("Please enter your name: ") # prompts user for name
print("This is the first input:", input1) # prints some string and entered in name from previous prompt


# Input Method 2
print('\n' * 2) # prints 2 new lines
print("***METHOD 2***")# prints method name

# loop control variable
control = True
while control: # while loop
    input2 = input("I am looking for specific input. You must type x: ") # prompts user for input
    # if the provided input is x , escape loop
    if input2 == "x": 
        control = False
# print below after the loop is escaped / broken
print("This is the second input: " + input2)


# Rewrite Input Method 2 so that no break statement is necessary 

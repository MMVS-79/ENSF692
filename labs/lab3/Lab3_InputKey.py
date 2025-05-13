# ENSF 692 Spring 2025
# May 13 Lab 3
# Exercise 3 - Solutions

# Add comments to explain the functionality of this program

# Input Method 1: single input
# Print a new line for spacing and then the method title
print('\n')
print("***METHOD 1***")
# Prompt the user to enter their name, input function will return the value as a string
input1 = input("Please enter your name: ") # Prompts for input
print("This is the first input:", input1) # Prints the original input back to the terminal along with a statement


# Input Method 2: continuous input via a while loop
print('\n' * 2) # Print two lines for spacing
print("***METHOD 2***")

# Loop continuously until exactly "x" is provided as the input
while True:
    input2 = input("I am looking for specific input. You must type x: ") # Prompt for user input
    if input2 == "x":
        break
print("This is the second input: " + input2) # Print original value to user


# Rewrite Input Method 2 so that no break statement is necessary 
print('\n' * 2)
print("***METHOD 2 AGAIN***")
input2 = 0
while input2 != "x":
    input2 = input("I am looking for specific input. You must type x: ")
print("This is the program input: " + input2)

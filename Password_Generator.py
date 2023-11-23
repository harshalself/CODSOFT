# Hello, HARSHAL here! This is a Python program to generate strong and random passwords for User.

# Import required Modules
import random
import math

# Start of Code
print("######### Password Generator using Python #########\n")

while True:
    # User input for Password Length
    pass_length = int(input("Enter Length of Password : "))

    # Password initialize to empty
    password = ""

    # To choose a character for the password from this character string
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    for i in range(pass_length):
        # This line generates a random number between 0 and the length of the characters string minus 1
        new = math.floor(random.random()*len(characters))
        password += characters[new]
    print("Random Generated Password is : ", password)

    # Ask user if he wants to use Password Generator again
    again = input("Would you like to calculate again(1.Yes/2.No) : ")
    if again != '1':
        break
# End of Code

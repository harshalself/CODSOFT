# Hello, HARSHAL here! This is a Python program to design a simple calculator to perform arithmatic operations.

# Start of code
print("######### Simple Calculator using Python #########\n")

# While loop to calculate again and again
while True:

    # Input 2 numbers from the user
    num1 = float(input("Enter the first number : "))
    num2 = float(input("Enter the second number : "))

    # Menu for operations
    print("\n*********** MENU ***********\nSelect operation to perform :")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # User input for operation choice
    choice = input("Enter choice : ")

    # Perform the selected operation
    if choice == '1':
        result = num1+num2
        print("Addition is ", result)
    elif choice == '2':
        result = num1-num2
        print("Subtraction is ", result)
    elif choice == '3':
        result = num1*num2
        print("Multiplication is ", result)
    elif choice == '4':
        if num2 != 0:
            result = num1/num2
            print("Division is ", result)
        else:
            print("Error: Cannot divide by zero")
    else:
        print("Invalid Choice. Please enter a valid choice")

    # Ask user if he wants to use calculator again
    again = input("Would you like to calculate again(1.Yes/2.No) : ")
    if again != '1':
        break
# End of code

# Hello, HARSHAL here! This is a Python program is a Stone Paper Scissor Game played between User and CPU.

# Import required Modules
import random

# Start of Code
print("***** Welcome to Rock, Paper, Scissors! *****")
user_score = 0
cpu_score = 0
while True:
    # Take input from user
    user_choice = input(
        "Enter your choice (rock, paper, or scissors) : ").lower()

    # CPU choice using random function
    cpu_choice = random.choice(['rock', 'paper', 'scissors'])

    # Print the choices
    print("You chose "+user_choice+" and CPU chose "+cpu_choice)

    # Compare choices
    if user_choice == cpu_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and cpu_choice == 'scissors') or \
         (user_choice == 'paper' and cpu_choice == 'rock') or \
         (user_choice == 'scissors' and cpu_choice == 'paper'):
        print("You win!")
        user_score = user_score+1
    else:
        print("CPU wins!")
        cpu_score = cpu_score+1

    # Display Scores
    print("Your Score : ", user_score)
    print("CPU Score : ", cpu_score)

    # Ask user if he wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
# End of Code

#RockPaperScissors
from time import sleep
import random

option_1 = "Rock"
option_2 = "Paper"
option_3 = "Scissors"

my_vars = [option_1, option_2, option_3]

print("Rock Paper Scissors")
sleep(0.5)
gameStart = input("Do you want to play? (y/n)")
while(gameStart != "y"):
    gameStart = input("Do you want to play? (y/n)")
sleep(0.5)
print("Great! Let's get started.")
sleep(0.5)
userChoice = input("Please enter your choice in lowercase (rock, paper, scissors): ")
while(userChoice != "rock" and userChoice != "paper" and userChoice != "scissors"):
    userChoice = input("Please enter your choice in lowercase(rock, paper, scissors): ")
print(f"Your choice: {userChoice}")
compChoice = random.choice(my_vars)
if userChoice == "rock":
    if compChoice == "Rock":
        print("Computer choice: Rock")
        print("It's a tie!")
    elif compChoice == "Paper":
        print("Computer choice: Paper")
        print("You lose!")
    elif compChoice == "Scissors":
        print("Computer choice: Scissors")
        print("You win!")
elif userChoice == "paper":
    if compChoice == "Rock":
        print("Computer choice: Rock")
        print("You win!")
    elif compChoice == "Paper":
        print("Computer choice: Paper")
        print("It's a tie!")
    elif compChoice == "Scissors":
        print("Computer choice: Scissors")
        print("You lose!")
elif userChoice == "scissors":
    if compChoice == "Rock":
        print("Computer choice: Rock")
        print("You lose!")
    elif compChoice == "Paper":
        print("Computer choice: Paper")
        print("You win!")
    elif compChoice == "Scissors":
        print("Computer choice: Scissors")
        print("It's a tie!")
print("Good game! Thanks for playing!")
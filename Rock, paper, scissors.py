#Rock paper scissors game by Immanuel, http://github.com/GitImmanuel, 11-07-2017
#Importing stuff
import time
import math
import random
import sys
import datetime

def neeeee():
    from datetime import datetime
    from datetime import time

    current = datetime.now()
    print('The current date and time is:', current)
    print('')

neeeee()

#Welcome
print("Welcome to my 'Rock, paper scissors' game.")
print('')
time.sleep(1)

print("Pick 'rock', 'paper' or 'scissors'.")

def randomyeah():
    return random.randint(1,3)


def computerpicks():
    computerPick = randomyeah()
    if computerPick == 1:
        print("Computer picked 'rock'!")
        print("")
        first()
    elif computerPick == 2:
        print("Computer picked 'paper'!")
        print("")
        second()
    elif computerPick == 3:
        print("Computer picked 'scissors'!")
        print("")
        last()

def picks():
    if userPick == "Rock" or userPick == "R" or userPick == "rock" or userPick == "r":
        print("You have chosen for 'rock'!")
        computerpicks()
    elif userPick == "Paper" or userPick == "P" or userPick == "p" or userPick == "paper":
        print("You have chosen for 'paper'!")
        computerpicks()
    elif userPick == "Scissors" or userPick == "S" or userPick == "scissors" or userPick == "s":
        print("You have chosen for 'scissors'!")
        computerpicks()
    else:
        print("Please choose 'rock', 'paper' or 'scissors'.")
        userpick()

def first():
    if userPick == "Rock" or userPick == "R" or userPick == "rock" or userPick == "r":
        print('Tie!')
        again()
    elif userPick == "Paper" or userPick == "P" or userPick == "p" or userPick == "paper":
        print('Congratulations! You won!')
        again()
    elif userPick == "Scissors" or userPick == "S" or userPick == "scissors" or userPick == "s":
        print("Ahw. You lost. :(")
        again()

def second():
    if userPick == "Rock" or userPick == "R" or userPick == "rock" or userPick == "r":
        print('Ahw. You lost. :(')
        again()
    elif userPick == "Paper" or userPick == "P" or userPick == "p" or userPick == "paper":
        print('Tie!')
        again()
    elif userPick == "Scissors" or userPick == "S" or userPick == "scissors" or userPick == "s":
        print("Congratulations! You won!")
        again()

def last():
    if userPick == "Rock" or userPick == "R" or userPick == "rock" or userPick == "r":
        print('Congratulations! You won!')
        again()
    elif userPick == "Paper" or userPick == "P" or userPick == "p" or userPick == "paper":
        print('Ahw. You lost. :(')
        again()
    elif userPick == "Scissors" or userPick == "S" or userPick == "scissors" or userPick == "s":
        print("Tie!")
        again()

def again():
    global againPlay
    againPlay = input('Do you want to play again? (y/n): ')
    print('')

    if againPlay == "y" or again == "Y" or again == "yes" or again == "Yes":
        print('Okay!')
        userpick()
    elif againPlay == "n" or again == "N" or again == "no" or again == "No":
        print('Thank you for playing my game!')
    else:
        print('Please answer yes or no.')
        again()

def userpick():
    global userPick
    userPick = input('Your pick: ')
    print('')
    picks()

userpick()

input("Exit terminal when done.")


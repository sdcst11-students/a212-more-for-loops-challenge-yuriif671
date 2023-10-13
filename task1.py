#!python3

'''
Create a number guessing game
There is a limit of 10 guesses
The program will ask the user to enter an integer from 1 to 100
The program will then tell the user if the number is too high, too low or correct.
If the number is correct, the program will end
If the 10 guesses are used up, the program will say that the user has lost
'''
import random

fail = True
goal = random.randint(1, 10)

for i in range(10):
    a = int(input("Gimme a number: "))

    if a < goal:
        print("Too low")
    elif a > goal:
        print("Too high")
    else:
        print("Yay!")    
        fail = False
        break 
    
if fail:
    print("You failed!")
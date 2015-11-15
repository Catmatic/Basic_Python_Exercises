#Write a guessing game where the user has to guess a secret number. After every guess the program tells the user whether their number was too large or too small. At the end the number of tries needed should be printed. I counts only as one try if they input the same number multiple times consecutively.

from random import randint

number = randint(0, 1000)
guess = 9001
guesslist = set()

print("\nWelcome to the arena, motherfucker! Guess a number until you get it right: \n")

while guess != number:
    guess = int(input("let's hear it. What's your guess? \n"))
    guesslist.add(guess)    
    if guess < number:
        print("\nToo small. Try again.\n")
    elif guess > number:
        print("\nToo large. Try again.\n")
        
tries = len(guesslist)

print("You did it! You got the answer by guessing {} unique numbers!".format(tries))

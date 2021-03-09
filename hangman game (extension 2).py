#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hangman Game (Extension Answers - turtles reading)

By: Monique Cheng
"""
# import random & turtle library
from random import randint
import turtle

# read the file with words (words.txt)
words_file = open("words.txt", "r")

# initialize word list
words = words_file.read().split('\n')

# create a function to find the indexes of letter guessed in the word
def letterFound(letter, word):
    index = []
    for i in range(len(word)):
        if (letter == word[i]):
            index.append(i)
    return index

# create a function to create a string from an array
def formWord(arr):
    string = ""
    for i in arr:
        string += i
    return string

# function to draw the hangman
def hangmanDraw(errors):
    if(errors == 1):
        turtle.setposition(100, -200)
        turtle.pendown()
        turtle.backward(200)
    elif(errors == 2):
        turtle.left(90)
        turtle.forward(400)
    elif(errors == 3):
        turtle.right(90)
        turtle.forward(200)
    elif(errors == 4):
        turtle.right(90)
        turtle.forward(40)
    elif(errors == 5):
        turtle.right(90)
        turtle.circle(50)
    elif(errors == 6):
        turtle.penup()
        turtle.left(90)
        turtle.forward(100)
        turtle.pendown()
        turtle.forward(150)
    elif(errors == 7):
        turtle.left(180)
        turtle.forward(95)
        turtle.right(120)
        turtle.forward(60)
    elif(errors == 8):
        turtle.left(180)
        turtle.forward(60)
        turtle.left(60)
        turtle.forward(60)
    elif(errors == 9):
        turtle.left(180)
        turtle.forward(60)
        turtle.right(120)
        turtle.forward(95)
        turtle.right(60)
        turtle.forward(60)
    else:
        turtle.left(180)
        turtle.forward(60)
        turtle.right(60)
        turtle.forward(60)

# use an infinite while loop, we will use 'break' to get out of this loop later
while (True):
    # set up turtle
    turtle.hideturtle()
    turtle.speed(100)
    turtle.penup()
    # initalize some variables
    wrong = 0
    lettersCorrect = 0
    lettersGuessed = []
    # select the random word through the randint() function
    word = words[randint(0, len(words) - 1)]
    # create the word the user sees
    wordSeen = []
    for i in range(len(word)):
        wordSeen.append( '_ ')
    print("Here is your word: " + formWord(wordSeen))
    # prompt the user to input their guess
    guess = input("Guess a letter: ")
    # if the guess is not a character, the user will be asked to guess the letter again
    while (len(guess) != 1):
        print("Please input a letter!")
        guess = input("Guess a letter: ")
    # another infinite loop while the user guesses the word
    while (True):
        # find where the letter guessed appears in the word
        # an array is returned with the indexes
        # if the letter doesn't appear, the array returned will be empty
        ind = letterFound(guess, word)
        # if the array is empty, the user was wrong...
        if (len(ind) == 0):
            wrong += 1
            lettersGuessed.append(guess)
            print("That letter is not in the word! You have " + str(10 - wrong) + " guesses.")
            hangmanDraw(wrong)
        # if the array wasn't empty the user was right...
        else:
            lettersGuessed.append(guess)
            # update the number of correctly guessed letters
            lettersCorrect += len(ind)
            # add the letters to the seen word in the correct indexes, and show this to the user!
            for i in ind:
                wordSeen[i] = guess
            print("Correct! That letter is in the word " + str(len(ind)) + " times!")
            print(formWord(wordSeen))
        # if the word has been guessed correctly, exit  the loop and notify the user
        if (lettersCorrect == len(word)):
            print("You guessed the word! Awesome job!")
            break
        # if the number of guesses has exceeded 10, exit the loop and notify the user
        # you can also tell the user the word!
        elif (wrong >= 10):
            print("You've exceeded the maximum number of guesses! The word was..." + word)
            break
        # else, continue letting the user guess
        else:
            print("The letters already guessed are:", lettersGuessed)
        # prompt the user to input their guess
        guess = input("Guess a letter: ")
        # we can also ensure the user hasn't guessed this letter before
        while ((guess in lettersGuessed) or len(guess) != 1):
            if (guess in lettersGuessed):
                print("You have already guessed this letter before! Guess a new one!")
            else:
                print("Please input a letter!")
            guess = input("Guess a letter: ")
    # set the variable tryAgain
    tryAgain = ""
    # while the user doesn't input 'yes' or 'no' as a response...
    while (tryAgain != "yes" and tryAgain != "no"):
        # prompt the user to input a response
        tryAgain = input("Would you like to try again? (yes or no)")
    # if the user inputs 'no', exit the while loop to end the game
    if (tryAgain == "no"):
        break
    turtle.reset()

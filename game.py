#importing some useful modules
import time
import sys
import os

#welcoming the user
print ("Hello, Time to play hangman! This is a test")
print("I hope that it works!")

# define a function for clearing the screen, no peeping!
def clear_screen():
    # here, we check if this game is run on a windows system, or other
    if sys.platform == "win32":
        # in a windows console, you type "cls" to clear the screen...
        command = "cls"
    else:
        # ... on linux or mac, you type "clear" instead
        command = "clear"
    # this will run that command and clear the screen
    os.system(command)


#wait for 1 second
time.sleep(1)

time.sleep(0.5)

userinput = input("Type in the hangman word for your choice: ")
type(userinput)
#here we set the secret

word = userinput


#creates an variable with an empty value
guesses = []

#determine the number of turns
turns = 11

# make a counter that starts with zero
failed = 0

# clear the screen so that the other person can't see the word
clear_screen()

print("The word is", len(word), "characters long!")
print("- " * len(word))

# Create a while loop

#check if the turns are more than zero
while turns > 0:

    # for every character in secret_word
    for char in word:

    # see if the character is in the players guess
        if char in guesses:

        # print then out the character
            print (char),

        else:

        # if not found, print a dash
            print ("not in word :("),

        # and increase the failed counter with one
            failed += 1

    # if failed is equal to zero

    # print You Won
    if failed == 0:
        print ("You won")

    # exit the script
        break

    print

    # ask the user go guess a character
    guess = input("guess a character:")

    # set the players guess to guesses
    guesses += guess

    # if the guess is not found in the secret word
    if guess not in word:

     # turns counter decreases with 1 (now 9)
        turns -= 1

    # print wrong
        print ("Wrong")

    # how many turns are left
        print ("You have", + turns, 'more guesses')

    # if the turns are equal to zero
        if turns == 0:

        # print "You Loose"
            print ("You Loose")

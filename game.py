#importing the time module
import time

#welcoming the user
print("Hello, Time to play hangman! This is a test")
print("I hope that it works!")


#wait for 1.5 second
time.sleep(1.5)

#here we set the secret

word = input("Type in the hangman word for your choice: ")


#creates an variable with an empty value
guesses = ''

#determine the number of failed guesses before you lose
failed = 0

# Create a while loop

#check if the failed are more than zero
while failed < 10:

    # ask the user go guess a character
    guess = input("guess a character:")

    # set the players guess to guesses
    guesses += guess

    correct = True

    # for every character in secret_word
    for char in word:

        # see if the character is in the players guess
        if char in guesses:

            # print then out the character
            print(char, end=''),

        else:

            # if not found, print a dash
            print("_", end=''),

            # and increase the failed counter with one
            correct = False

    # if failed is equal to zero
    print('')
    # print You Won
    if correct:
        print("You won")

        # exit the script
        break

    # if the guess is not found in the secret word
    if guess not in word:

        
        failed += 1

        # print wrong
        print("Wrong")

        # how many failures are left
        print("You have", 10 - failed, 'more guesses')

        # if the failed are equal to zero
        if failed > 9:

            # print "You Loose"
            print("You Loose")

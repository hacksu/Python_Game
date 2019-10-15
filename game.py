#importing the time module
import time

#welcoming the user
print ("Hello, Time to play hangman! This is a test")
print("I hope that it works!")


#wait for 1 second
time.sleep(1)

time.sleep(0.5)

run = True

while run:

    userinput = input("Type in the hangman word for your choice: ")
    type(userinput)
    #here we set the secret

    word = userinput

    again = ''

    #creates an variable with an empty value
    guesses = ''

    #determine the number of turns
    turns = 10

    # Create a while loop

    #check if the turns are more than zero
    while turns > 0:

        # make a counter that starts with zero
        failed = 0

        # for every character in secret_word
        for char in word:

        # see if the character is in the players guess
            if char in guesses:

            # print then out the character
                print (char),

            else:

            # if not found, print a dash
                print ("_"),

            # and increase the failed counter with one
                failed += 1

        # if failed is equal to zero

        # print You Won, asks to play again
        if failed == 0:
            print ("You won. Play again? [y/n]")
            again = input()

        # Reloops if play again, otherwise exit
            if again == 'n':
                print('Thanks for playing!')
                run = False
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

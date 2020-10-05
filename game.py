import getpass

#welcoming the user
print("Hello, Time to play hangman! This is a test")
print("I hope that it works!")


# using getpass module to hide the word given by host from the solver
userinput = getpass.getpass("Type in the hangman word of your choice: ")

# making the puzzle
word = ""
if len(userinput) <= 7 and len(userinput) > 0:
    for i in range(0, len(userinput)):
        if i%2 == 0:
            word += "_ "
        else:
            word += userinput[i] + " "

else:
    for i in range(0, len(userinput)):
        if i%3 == 0:
            word += userinput[i] + " "
        else:
            word += "_ "

print(word.upper())

#creates a variable with an empty value
guesses = ''

#determine the number of turns
turns = len(userinput)

# Create a while loop

#check if the turns are more than zero
while turns > 0:

    # ask the user go guess a character
    guess = input("Guess a character: ")

    # set the players guess to guesses
    guesses += guess

    # if the guess is not found in the secret word
    if guess not in userinput:

    # turns counter decreases by 1
        turns -= 1

    # print wrong
        print("Wrong")

    # how many turns are left
        print("You have " + str(turns) + 'more guesses left')

    # if the turns are equal to zero
        if turns == 0:

        # print "You Lose"
            print("You lose")
            break


    # make a counter that starts with zero
    failed = 0

    # for every character in secret_word
    for char in word:

    # see if the character is in the players guess
        if char in guesses and char is not " " and char is not "_":

        # print then out the character
            print(char, end = "")

        else:

        # if not found, print a dash
            print()
 
        # and increase the failed counter with one
            failed += 1

    # if failed is equal to zero

    # print You Won
    if failed == 0:
        print ("You won")

    # exit the script
        break

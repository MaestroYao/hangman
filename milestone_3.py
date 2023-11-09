import random
'''
Milestone 3, this milestone develops some pieces of code and then it allows us to encapsulate them more organised as functions

-- Task 1
Step 1:
Create a while loop and set the condition to True.

Step 2:
Ask the user to guess a letter and assign this to a variable called guess.

Step 3:
Check that the guess is a single alphabetical character.

Step 4:
If the guess passes the checks, break out of the loop.

Step 5:
If the guess does not pass the checks, then print a message saying "Invalid letter. Please, enter a single alphabetical character."

'''

while True:
    guess = input("Guess a letter: ")

    if (len(guess)==1) and (guess.isalpha()== True):
        break
    
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")


'''
-- Task 2
Step 1:
Create an if statement that checks if the guess is in the word.


Step 2:
In the body of the if statement, print "Good guess! {guess} is in the word.".


Step 3:
Create an else block that prints "Sorry, {guess} is not in the word. Try again."
'''

word_list = ["orange", "banana", "mango", "coconut", "pineapple"]
word = random.choice(word_list)

if guess in word:
    print("Good guess! '" + guess+ "' is in the word.")
else:
    print("Sorry, '" + guess + "' is not in the word.")
    

'''
Task 3

Create 2 functions, check_guess and ask_for_input

FOR CHECK_GUESS:
Step 1:
Define a function called check_guess. Pass guess as a parameter for the function.

Step 2:
Convert the guess into lower case.


Step 3:
Move the code that you wrote to check if the guess is in the word into this function block.


FOR ASK_FOR_INPUT:


Step 1:
Define a function called ask_for_input.


Step 2:
Move the code that you wrote in the Iteratively check if the input is a valid guess task into this function block.


Step 3:
Outside the while loop, call the check_guess function to check if the guess is in the word.


Step 4:
Outside the function, call the ask_for_input function to test your code.

'''


word_list = ["orange", "banana", "mango", "coconut", "pineapple"]
word = random.choice(word_list)


def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print("Good guess! '" + guess+ "' is in the word.")
    else:
        print("Sorry, '" + guess + "' is not in the word.")


def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        if (len(guess)==1) and (guess.isalpha()== True):
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

    check_guess(guess)




ask_for_input()

        


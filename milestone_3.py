'''
Milestone 3 -- Task 1


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
        


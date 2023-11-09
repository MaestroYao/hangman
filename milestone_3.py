import random
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

        


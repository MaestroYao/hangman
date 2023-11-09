import random

'''
Milestone 2 -- Task 1 
Step 1. Create a List of 5 fruits
Step 2. Assign it to a variable
Step 3. Print the list
'''
word_list = ["mango","pineapple","passion fruit","coconut","orange"] 
print(word_list)



'''
Task 2
Step 1. Import randome module in the first line of code
Step 2. Create the random.choice method and pass it the word_list variable
Step 3: Assign the randomly generated word to a variable called word.
Step 4: Print the word variable
'''

word = random.choice(word_list)
print(word)

'''
Task 3
Step 1: Using the input function, ask the user to enter a single letter.
Step 2: Assign the input to a variable called guess.
'''
guess = input('Enter one single letter: ')


'''
Task 4
Step 1: Check if the length of the input is equal to 1 and alphabetical.
Step 2: If the input is valid print "Good guess!".
Step 3: Else print "Oops! That is not a valid output"
'''

if (len(guess)== 1) and (guess.isalpha()== True):
    print("Good guess!")
    
else:
    print("Oops! That is not a valid output")

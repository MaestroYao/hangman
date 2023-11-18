import random

class Hangman:
    word_list = ["banana","apple","orange","strawberry","mango"]
    word = random.choice(word_list)
    word_guessed = ["_" for i in word]
    list_of_guesses = []
    num_letters = len(set(list(word)))
    num_lives = 5
    print(word)
    print(word_guessed)
    
    
    def __init__(self, word_list, num_lives = 5):
        
        self.list_of_guesses = None


    def check_guess(guess):
            guess = guess.lower()
            word = Hangman.word
            word_guessed = Hangman.word_guessed
            num_letters = Hangman.num_letters
            num_lives = Hangman.num_lives
            count = 0
            if guess in word:
                

                print("Good guess! '" + guess + "' is in the word.")
                for each_letter in list(word):

                    if each_letter == guess:
                        word_guessed[count] = guess
                    count = count +1
                print(word_guessed)
                num_letters = num_letters - 1
                
            else:
                print("Sorry, '" + guess + "' is not in the word.")
                num_lives = num_lives - 1
                print("You have ", num_lives, " lives left.")
                        
                    
                  


    def ask_for_input():
        list_of_guesses = Hangman.list_of_guesses
        guess = None
        while True:
            guess = input("Guess a letter: ")
            if (len(guess)>1) or (guess.isalpha()== False):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif (guess in list_of_guesses):
                print("You already tried that letter!")
            else:

                Hangman.check_guess(guess)
                list_of_guesses.append(guess)

                
'''
                    
'''

Hangman.ask_for_input()

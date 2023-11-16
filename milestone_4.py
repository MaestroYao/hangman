import random

class Hangman:
    word_list = ["banana","apple","orange","strawberry","mango"]
    word = random.choice(word_list)
    list_of_guesses = []
    print(word)
    
    def __init__(self, word_list, num_lives = 5):
        
        self.num_lives = 5
        self.list_of_guesses = None
        self.word_guessed = None
        self.num_letters = None


    def check_guess(guess):
            guess = guess.lower()
            word = Hangman.word
            if guess in word:
                print("Good guess! '" + guess + "' is in the word.")
            else:
                print("Sorry, '" + guess + "' is not in the word.")

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
                print(guess)
                Hangman.check_guess(guess)
                list_of_guesses.append(guess)
                print(list_of_guesses)


Hangman.ask_for_input()


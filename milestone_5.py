import random

class Hangman:
    
    def __init__(self, word_list, num_lives):

        self.word_list = word_list
        self.num_lives = num_lives

        
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for i in self.word]
        self.num_letters = len(set(list(self.word)))
        self.list_of_guesses = []

        pass
        


    def check_guess(self, guess):
            guess = guess.lower()

            count = 0
            if guess in self.word:
                print("Good guess! '" + guess + "' is in the word.")
                for each_letter in list(self.word):

                    if each_letter == guess:
                        self.word_guessed[count] = guess
                    count = count +1
                print(self.word_guessed)
                
                self.num_letters = self.num_letters - 1
        
                
            else:
                print("Sorry, '" + guess + "' is not in the word.")
                self.num_lives = self.num_lives - 1
                print("You have ", self.num_lives, " lives left.")

            pass
                        
                    
                  


    def ask_for_input(self):
        
        while True:
            guess = input("Guess a letter: ")
            if (len(guess)>1) or (guess.isalpha()== False):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif (guess in self.list_of_guesses):
                print("You already tried that letter!")
            else:

                Hangman.check_guess(self, guess)
                self.list_of_guesses.append(guess)
                break
        pass



def play_game(word_list):

    num_lives = 5
    game = Hangman(word_list, num_lives)
    

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif (game.num_letters == 0) and (game.num_lives !=0):
            print("Congratulations. You won the game!")
            break
    pass

                

word_list = ["grape", "peach", "banana", "cherry", "apple"]
play_game(word_list)
            
        

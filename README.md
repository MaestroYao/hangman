# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 
The aim of this implementation is to develop my programming techniques as well as get an understanding of the use of GitHub and the workflow it offers.
In this readme, my aim is to document the process I undertook in each Milestone to develop my version of the game

### Milestone 1
In this Milestone I had to first set up a Github repository for the game files. This was easily done by the AiCore webpage which created it automatically.

### Milestone 2
For this activity I had to start doing some basics of programming such as creating a list of words and choosing a random word from it, asking the user for single-character input. All of these tasks also involved if-else statements and while loops to create iteration when asking for input.

### Milestone 3
Furthermore, I had to create a statement that iteratively would check if the input the user is providing is valid for the game so as to catch possible bugs, and then also check if the guessed letter is in the randomly selected word as this is needed for the game to progress. Both of these checks then are programmed into functions so that they can be better understood and explained within the program.

### Milestone 4
Then, the functions I previously created can be used as part of the Hangman class which encapsulates the main methods of the game. In each section of the class methods occur which divide what different things the class does. First, all attributes are initialized using __init__ method. Additionally, we have the other 2 methods which are the functions created in Milestone 3, for checking the guess and deciding and asking the user for valid input.

### Milestone 5
In this milestone, the code is finalized to have a fully functional version of the game. First, we code a final function on the main of the program outside of the class which initializes an instance of the class Hangman and therefore runs the game. This function also states the number of lives the user has in the game and stops the game if the user loses all of them, as well as states if the user has won when all letters of the word have been discovered and they still have lives, finally if neither conditions are met the function keeps asking for input from the user to keep the game going.

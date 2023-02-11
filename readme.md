# Coder Academy T1A3 - Terminal Application

```python
     _____            _           _        _    _
    |  __ \          | |         (_)      | |  | |
    | |  | |_   _ ___| | _____  ___  ___  | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
    | |  | | | | / __| |/ _ \ \/ / |/ __| |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |__| | |_| \__ \ |  __/>  <| | (__  | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_____/ \__, |___/_|\___/_/\_\_|\___| |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
             __/ |                                             __/ |
             |___/                                             |___/
```
---

## Introduction

This code implements a dyslexic hangman game in Python. It generates a random word from a word list and shuffles the 
letters. The game also includes a riddle that provides a clue for the user to the word to be guessed. 
The game uses a CSV file to store the words and riddles.

The game starts with displaying ASCII art of the title ```Dyslexic Hangman``` and welcomes the user to the game. The game 
then displays the shuffled word in the form of underscores, with each underscore representing a letter in the word, 
but remember; the letters are out of order.

The user is prompted to guess a letter, and if the letter is in the word, the corresponding underscores are replaced 
with the letter. If the letter is not in the word, the user loses a life and the hangman ASCII art is updated to 
reflect the lives remaining. The game ends when either the word has been successfully guessed or the user has lost all 
their lives. The user also has the option to exit the game at any time by entering "0".

---

## Features

1. **Random Word Generation:** A random word is selected from a pre-defined word list, ```hangman1_wordList.word_list```, 
   using the ```random.choice()``` method. 
2. **Dyslexic Letter Shuffle:** The selected word is converted to a list, the letters are shuffled using ```random.
   shuffle()``` method and then converted back to a string. 
3. **Riddle Clue:** A riddle is generated as a clue to the word to be guessed. The code uses a CSV file```hangman1_clue.csv``` 
to search for the randomly generated word, and if a match is found, the corresponding riddle is displayed to the user. 
4. **Game Play Loop:** The game play loop is implemented using a while loop that continues until the user either 
correctly guesses the word or runs out of lives. The user is prompted to guess a letter, and the code checks if the 
letter is in the word. If the letter is in the word, the corresponding underscores are replaced with the letter. If the letter is 
not in the word, the user loses a life, and the hangman ASCII art is updated. 
5. **End Game Condition:** The while loop breaks out when either all the letters in the word have been correctly 
   guessed, 
or the user runs out of lives. In the first case, the user wins, and in the second case, the user loses. 
6. **ASCII Art:** The code uses ASCII art to represent the hangman stages, which is imported from the hangman1_ascii 
   module.

---

## Installation

> **Todo:** Add installation instructions


---

## Game Play Instructions

1. You will be playing a Hangman game with a twist. The letters in the word are shuffled.
2. The game will randomly choose a word from a word list. 
3. The game will shuffle the letters in the chosen word. 
4. You have 6 lives to guess the word. 
5. The game will display a riddle to help you guess the word and therefor the letters. 
6. You will need to guess a letter by entering it on the key pad. If you wish to quit the game, you can enter the
 number ```0``` and press ```Enter```. 
7. If you have already guessed the letter, the game will display the message ```You have already guessed that letter```. 
8. If you entered a single letter, the game will check if the letter is in the word. If the letter is in the
word, the game will replace the underscore with the letter. If the letter is not in the word, the game will remove a life. 
9. If you run out of lives, you lose the game. If you correctly guess all the letters in the word, you win the game. 
10. The game will display ASCII art of the Hangman at each stage as you guess the letters in the word.
11. **Remember**, the letters are out of order. 
12. Winning the game will display the Word with the letters in correct order. Good luck!

<br>

## Code explanation - Iterative Steps

1. The code ```imports``` the required libraries, ```csv```, ```random```, ```hangman1_wordList```, and ```hangman1_ascii```. 
2. The ```play_game``` function is defined, which contains the core logic of the hangman game. 
3. The function generates a random word from the list of words in the ```hangman1_wordList``` module. 
4. The randomly generated word is then shuffled to create a dyslexic version of the word. 
5. The game displays an introduction to the user and sets the number of lives to 6. 
6. The function opens a CSV file named hangman1_clue.csv and uses the csv library to read the file.
7. The function searches the file for the word that was randomly generated and prints a riddle for the word if a match 
is found.
8. The function enters a game loop, where the user is asked to guess a letter or quit the game. 
9. If the user has already guessed the letter, an error message is displayed. 
10. If the user inputs 0, the game exits. 
11. If the user inputs a letter, the function checks if it is in the word. If it is, the letter is added to the display 
word. If not, a life is lost. 
12. If the display word is filled with letters and there are no more underscores, the user has won the game.
If the number of lives reaches 0, the user loses the game. 
13. The function continues to run the game loop until the user wins or loses the game, or quits the game.





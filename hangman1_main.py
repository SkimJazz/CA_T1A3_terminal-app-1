# : Coder Academy - T1A3 Terminal Application
# : Joshua Bennett
# : ID 13399
# : February 2023
# : Hangman Game
# : This project is assignment-3 of term-1 for Coder Academy standard delivery. Ref to the README.md file for more
# : information.


# : STEP 1 - Generate a random word from a list of words
# ====================================================================================================

# : Todo-1: Add a list of words to the game

import random

wordList = [
    'eagle',
    'penguin',
    'wolf',
]

# : Todo-2: Add a random word generator
randomWord = random.choice(wordList)

# : Todo-3: Ask the user to guess a letter
    # : todo-3.1: need user input with a prompt
    # : todo-3.2: convert the user input to lower case
    # : todo-3.3: store the user input in a variable
    # : todo-3.4: check if the user input is a letter
        # : todo-3.4.1: if not a letter, ask the user to enter a letter

# Error handling for user input-> only letters allowed
while True:

    # User input and validation
    uGuess = input("Guess a letter: ").lower()

    # 'isalpha' checks if the input is a letter -> iSO & Linux compatible method
    if uGuess.isalpha() and len(uGuess) == 1:

        # break out of the loop if the input is valid
        break
    print("Invalid input. Please enter a single letter.")

# uGuess = input("Guess a letter: ").lower()

# : Todo-4: Check if the letter is in the word
    # : todo-4.1: loop through the randomWord using a for loop
    # : todo-4.2: check if the letter is in the randomWord
    # : todo-4.2.1: if the letter is in the randomWord, print a message
    # : todo-4.2.2: else letter is not in the randomWord, print a message

for letter in randomWord:
    if letter == uGuess:
        print("Correct! You guessed a letter")
    else:
        print("Incorrect! Try again")

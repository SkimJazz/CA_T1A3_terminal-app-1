# : Coder Academy - T1A3 Terminal Application
# : Joshua Bennett
# : ID 13399
# : February 2023
# : Hangman Game
# : This project is assignment-3 of term-1 for Coder Academy standard delivery. Ref to the README.md file for more
# : information.


import random
import hangman1_wordList
from hangman1_ascii import intro, stage


genWord = random.choice(hangman1_wordList.wordList)


wordLength = len(genWord)


# : User lives
lives = 6


# : Display intro -> Dyslexic Hangman
print(intro)


# : Test the random word generator and user input
print(f"Word test is: {genWord}")

# : Create a list of underscores(blanks) to display to user
displayWord = []
for _ in range(wordLength):
    displayWord += "_"

endGame = False

# : Game play loop
while not endGame:

    # : User input for letter guess and exiting game
    uGuess = input("Guess a letter or press 'Zero' and 'Enter' to quit game: ").lower()

    if uGuess in displayWord:
        print("You already guessed that letter")

    # : User option to exit game at letter guessing stage
    # : Cant use a letter as a break-out condition as letter could be in the word list
    if uGuess == "0":
        print("Yeah Nice! Catch ya next time")
        endGame = True
        break

    # : User input error handling-> letters only-> 'isalpha()' Linux/iSO compatible method
    if uGuess.isalpha() and len(uGuess) == 1:

        # : Cross-reference user letter guess with letter in genWord
        for letterPosition in range(wordLength):
            letter = genWord[letterPosition]

            # : If the letter is in word, replace the underscore with the letter
            if letter == uGuess:
                displayWord[letterPosition] = letter

        print(" ".join(displayWord))

        # : If the letter is not in the word, remove a life
        if uGuess not in genWord:
            print(f"You guessed {uGuess}, that's not in the word. You lose a life")
            lives -= 1
            if lives == 0:
                endGame = True
                print("You lose!")

        # : While loop BREAK OUT condition -> if no more underscores in the displayWord list, user has won game
        elif "_" not in displayWord:
            endGame = True
            print("You win!")

        # : Method - using 'from hangman1_ascii import stage' and calling the stages from hangman1_ascii.py
        print(stage[lives])

    else:
        print("Invalid input. Please enter a single letter.")

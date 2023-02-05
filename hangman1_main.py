# : Coder Academy - T1A3 Terminal Application
# : Joshua Bennett
# : ID 13399
# : February 2023
# : Hangman Game
# : This project is assignment-3 of term-1 for Coder Academy standard delivery. Ref to the README.md file for more
# : information.


# : Todo 1-2.1: Add import random to generate random word
import random
import hangman1_wordList
# import hangman1_ascii
# import pandas -> Using Pandas to read from CSV file. CSV file will contain a Riddle for each word in the wordList
#                The riddle and matching word will be accessed and stored in a dictionary.


# : Todo 1-2: Add a random word generator
genWord = random.choice(hangman1_wordList.wordList)

wordLength = len(genWord)

# : Test the random word generator and user input
print(f"Word test is: {genWord}")

# : Create a list of underscores(blanks) to display to user
displayWord = []
for _ in range(wordLength):
    displayWord += "_"

endGame = False

while not endGame:

    # : user input for letter guess and exiting game
    uGuess = input("Guess a letter or type 'exit' to quit game: ").lower()

    # : game exit
    if uGuess == "exit":
        print("Yeah Nice! Catch ya next time")
        endGame = True
        break

    # : user input error handling-> letters only-> 'isalpha()' Linux/iSO compatible method
    if uGuess.isalpha() and len(uGuess) == 1:

        # : cross-reference users letter guess with letter in genWord
        for letterPosition in range(wordLength):
            letter = genWord[letterPosition]

            # : if the letter is in the word, replace the underscore with the letter
            if letter == uGuess:
                displayWord[letterPosition] = letter

        print(displayWord)

        # NOTE: CAREFUL this can easily end up as a 'infinite loop' if the condition is not met.
        # A while loop requires some sort of change that changes the condition that the loop is dependent on to
        # break out of loop. In this case, if there are no more underscores in the displayWord list, the user has won
        if "_" not in displayWord:
            endGame = True
            print("You win!")

    else:
        print("Invalid input. Please enter a single letter.")

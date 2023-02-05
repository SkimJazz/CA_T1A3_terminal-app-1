# : Coder Academy - T1A3 Terminal Application
# : Joshua Bennett
# : ID 13399
# : February 2023
# : Hangman Game
# : This project is assignment-3 of term-1 for Coder Academy standard delivery. Ref to the README.md file for more
# : information.


# : Todo 1-2.1: Add import random to generate random word
import random


# : Todo 1-1: Add a list of words to the game
wordList = ['eagle', 'penguin', 'wolf',]


# : Todo 1-2: Add a random word generator
genWord = random.choice(wordList)

wordLength = len(genWord)

# : Todo 1-3: Ask the user to guess a letter
    # : todo 1-3.1: need user input with a prompt
    # : todo 1-3.2: convert the user input to lower case
    # : todo 1-3.3: store the user input in a variable
    # : todo 1-3.4: check if the user input is a letter
        # : todo 1-3.4.1: if not a letter, ask the user to enter a letter


# : Test the random word generator and user input
print(f"{genWord}")

displayWord = []

for _ in range(wordLength):
    displayWord += "_"

print(displayWord)


# Error handling for user input-> only letters allowed
# while True:
#     # User input and validation accounting for case sensitivity and Linux/iSO compatibility
#     uGuess = input("Guess a letter: ").lower()
#     # 'isalpha' checks if the input is a letter -> Linux/iSO compatible method
#     if uGuess.isalpha() and len(uGuess) == 1:
#         # break out of the loop if input is valid
#         break
#     print("Invalid input. Please enter a single letter.")


endGame = False


while not endGame:

    uGuess = input("Guess a letter: ").lower()

    for letPosition in range(wordLength):
        letter = genWord[letPosition]
        if letter == uGuess:
            displayWord[letPosition] = letter

            print("Correct! You guessed a letter")
        else:
            print("Incorrect! Try again")

    print(displayWord)

    # NOTE: CAREFUL this can easily end up as a 'infinite loop' if the condition is not met.
    # A while loop requires some sort of change that changes the condition that the loop is dependent on to
    # break out of the loop. In this case, if there are no more underscores in the displayWord list, the user has won
    if "_" not in displayWord:
        endGame = True
        print("You win!")



# for letPosition in range(len(genWord)):
#     letter = genWord[letPosition]
#     if letter == uGuess:
#         displayWord[letPosition] = letter
#         print("Correct! You guessed a letter")
#     else:
#         print("Incorrect! Try again")
#
# print(displayWord)

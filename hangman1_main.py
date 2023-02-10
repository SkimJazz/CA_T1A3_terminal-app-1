# : Coder Academy - T1A3 Terminal Application
# : Joshua Bennett
# : ID 13399
# : February 2023
# : Hangman Game
# : This project is assignment-3 of term-1 for Coder Academy standard delivery. Ref to the README.md file for more
# : information.


import csv
import random
import hangman1_wordList
from hangman1_ascii import intro, stage


def play_game():
    # : Generate a random word from the wordList
    gen_word = random.choice(hangman1_wordList.word_list)

    # ============= Dyslexic letter shuffle of random word =============

    # : Convert the randomly generated word to a list
    word_list = list(gen_word)

    # : Shuffle letters in the list
    random.shuffle(word_list)

    # : Convert the shuffled letters back to a string
    shuffled_word = "".join(word_list)

    # : Get the length of shuffled word
    word_length = len(shuffled_word)

    # : User lives
    lives = 6

    # : Display intro -> Dyslexic Hangman
    print("\nHey! Welcome to")
    print(intro)
    print("\nThis Hangman game has a twist. The letters in the word are shuffled. Good luck!")

    # : ERROR handling -> random word generator -> ref hangman1_test.py for function test
    # print(f"Word test is: {gen_word}")

    # : Create a list of underscores(blanks) to display to user
    display_word = []
    for _ in range(word_length):
        display_word += "_"

    end_game = False

    # : =================== Read CSV file ====================

    with open('hangman1_clue.csv', "r") as read_obj:
        reader = csv.DictReader(read_obj)
        rows = list(reader)

        # : Search for the word in the CSV file
        match_found = False

        # : Initialize var or PyCharm will lose its shit
        riddle = ""

        # : Iterate over each row in the csv using reader object
        for row in rows:

            # : Check if random genWord matches the word in the CSV file
            if row['word'] == gen_word:

                match_found = True

                # : ERROR handling -> read from csv -> Get id, word, riddle from row
                # key = row.get('id')   # output = None
                # word = row['word']
                riddle = row['riddle']
                break

        # : Print riddle if match found
        if match_found:
            # print("id:", key)
            # print("Word:", word)
            print("\nHere's a riddle:", "\n")
            print(riddle)
            print("\nwhat am I?")

        # : ERROR handling -> message if match not found
        else:
            print("Match not found.")

    # : =================== Game play loop ====================

    while not end_game:

        # : User input for letter guess and exiting game
        u_guess = input("\nGuess a letter or press 'Zero' and 'Enter' to quit game: ").lower()

        # : Error handling for already guessed letters
        if u_guess in display_word:
            print("You already guessed that letter")

        # : EXIT game option at letter guessing stage
        # : Cant use letters as a break-out condition, as letter could be in the word list
        if u_guess == "0":
            print("Yeah Nice! Catch ya next time")
            # end_game = True  # : Not needed -> entering '0' will break out of the loop
            break

        # : User input error handling-> letters only-> 'isalpha()' Linux/iSO compatible method
        if u_guess.isalpha() and len(u_guess) == 1:

            # : Cross-reference user letter guess with letter in gen_word
            for letter_position in range(word_length):

                # : Get letter at the position
                letter = shuffled_word[letter_position]

                # : If the letter is in word, replace the underscore with the letter
                if letter == u_guess:
                    display_word[letter_position] = letter

            # : Print the display_word list as a string
            print(" ".join(display_word))

            # : If the letter not in word -> remove a life
            if u_guess not in gen_word:
                print(f"You guessed {u_guess}, that's not in the word. You lose a life")
                lives -= 1
                if lives == 0:
                    end_game = True
                    print("You lose!")

            # : While loop BREAK OUT condition -> if no more underscores in display_word list, user has won game
            elif "_" not in display_word:
                end_game = True
                print(f"You win! The word was {gen_word}")

            # : Method - using 'from hangman1_ascii import stage' and calling the stages from hangman1_ascii.py
            print(stage[lives])

        else:
            print("Invalid input. Please enter a single letter.")


if __name__ == "__main__":
    play_game()

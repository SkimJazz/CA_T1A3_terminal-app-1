# : Coder Academy - T1A3 Terminal Application
# : Joshua Bennett
# : ID 13399
# : February 2023
# : Hangman Game
# : This project is assignment-3 of term-1 for Coder Academy standard delivery. Ref to the README.md file for more
# : information.


import csv
import hangman1_wordList
import random
from hangman1_ascii import intro, stage


def play_game():
    # : =================== ASCII art Intro ====================

    print("\nHey! Welcome to")
    print(intro)
    print("\nThis Hangman game has a twist. The letters in the word are shuffled. Good luck!")

    # : =================== Dyslexic letter shuffle ====================

    # : Randomly select a word from the wordList
    gen_word = random.choice(hangman1_wordList.word_list)

    # : Convert the randomly generated word to a list
    word_list = list(gen_word)

    # : Shuffle letters in the list
    random.shuffle(word_list)

    # : Convert the shuffled letters back to a string
    shuffled_word = "".join(word_list)

    # : Get the length of shuffled word
    word_length = len(shuffled_word)

    display_word = []
    for _ in range(word_length):
        display_word += "_"

    # print(f"Word test is: {gen_word}") # : ERROR handling -> random word generator

    # : =================== Game variables ====================

    end_game = False

    # : stages of ASCII art
    lives = 6

    # : =================== Read CSV file ====================

    with open('hangman1_clue.csv', "r") as read_obj:
        reader = csv.DictReader(read_obj)
        rows = list(reader)

        # : Search for word in CSV file
        match_found = False

        # : Initialize var to store riddle
        riddle = ""

        # : Iterate over each row in csv using reader object
        for row in rows:
            # : Check random word matches word in CSV file
            if row['word'] == gen_word:
                match_found = True

                # : Read from CSV file
                riddle = row['riddle']
                break

        # : ERROR handling PASS -> display riddle if match found
        if match_found:
            print("\nHere's a riddle:", "\n")
            print(riddle)
            print("\nwhat am I?")

        # : ERROR handling FAIL -> message if match not found
        else:
            print("Match not found.")

    # : =================== Game play loop ====================

    while not end_game:

        # : User guess input
        u_guess = input("\nGuess a letter or press 'Zero' and 'Enter' to quit game: ").lower()

        # : ERROR handling -> already guessed letters
        if u_guess in display_word:
            print("You already guessed that letter")

        # : EXIT game option -> can't use letters as a break-out condition
        elif u_guess == "0":
            print("Yeah Nice! Catch ya next time")
            # end_game = True  # : Not needed
            break

        # : ERROR handling -> letters only-> 'isalpha()' Linux/iSO compatible method
        if u_guess.isalpha() and len(u_guess) == 1:

            # : Cross-reference letter guess with letters in word
            for letter_position in range(word_length):

                # : Get letter position
                letter = shuffled_word[letter_position]

                # : If letter in word, replace underscore with letter
                if letter == u_guess:
                    display_word[letter_position] = letter

            # : Print the display_word list as a string
            print(" ".join(display_word))

            # : If letter not in word -> remove a life
            if u_guess not in gen_word:
                print(f"You guessed {u_guess}, that's not in the word. You lose a life")
                lives -= 1
                if lives == 0:
                    end_game = True
                    print("You lose!")

            # : While loop BREAK OUT condition -> if no more underscores in display_word list, user won game
            elif "_" not in display_word:
                end_game = True
                print(f"You win! The word was {gen_word}")

            # : Method - using 'from hangman1_ascii import stage' and calling the stages from hangman1_ascii.py
            print(stage[lives])

        else:
            print("Invalid input. Please enter a single letter.")


if __name__ == "__main__":
    play_game()

# : =================== End of file ====================

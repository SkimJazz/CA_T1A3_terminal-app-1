import hangman1_main
import hangman1_wordList


# : =================== Test-1 Automated ====================

# Testing the correct word being randomly selected from the word list

# : define a test function called test_random_word_selected
def test_random_word():
    # : Select a word from the word list using the random.choice method and store it in the gen_word variable.
    gen_word = hangman1_main.random.choice(hangman1_wordList.word_list)

    # : Use an assert statement to check if the gen_word is in the wordList list.
    assert gen_word in hangman1_wordList.word_list

    # : Run the test with pytest -> pytest hangman1_test.py


# : =================== Test-2 Manual Testing ====================

# Testing the user's ability to guess a correct letter:


# : Win scenario:

# Start the game by running the hangman1_main.py file.
# Observe the display_word which should contain underscores representing the length of the word to be guessed.
# Input a letter in the guessing field.
# Check if the letter appears in the display_word.
# Repeat the process until you win the game.

# : Lose scenario:

# Repeat the process until you lose the game
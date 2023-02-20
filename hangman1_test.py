import csv
import random
import hangman1_wordList
import hangman1_main


# : =================== Test-1 Random Word Generation ====================

# Testing the correct word being randomly selected from the word list

def test_random_word():
    gen_word = hangman1_main.random.choice(hangman1_wordList.word_list)
    assert gen_word in hangman1_wordList.word_list


# : =================== Test-2 Dyslexic Letter Shuffle ====================

def test_letter_shuffle():
    gen_word = hangman1_main.random.choice(hangman1_wordList.word_list)
    word_list = list(gen_word)
    random.shuffle(word_list)
    assert word_list != gen_word


# : =================== Test-3 Riddle Clue ====================

# Read the CSV file once and store the rows in a global variable
with open('hangman1_clue.csv', "r") as read_obj:
    reader = csv.DictReader(read_obj)
    clue_rows = list(reader)


def test_riddle_clue():
    gen_word = hangman1_main.random.choice(hangman1_wordList.word_list)
    clue = [row['riddle'] for row in clue_rows if row['word'] == gen_word]
    assert clue, f"No clue found for word '{gen_word}' in hangman1_clue.csv"


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

## Links

- [GitHub Repository](https://github.com/SkimJazz/CA_T1A3_terminal-app-1)
- [Readme Documentation](https://github.com/SkimJazz/CA_T1A3_terminal-app-1/blob/main/readme.md)
- [Presentation Video - YouTube](https://youtu.be/OPaGd6nUGiE)

---

## Tech Stack

- Python 3.11.0 - Programming Language
- Pytest 6.2.5 - Testing
- Windows 10 - Operating System
- PyCharm IDE - To write and test code
- Git and GitHub - Version Control & Documentation
- Trello - Project Management
- ClipChamp - Video Presentation
- YouTube - Presentation Hosting
- MS Powerpoint - Slide Deck

---

## Style Guide

This Terminal Application follows the PEP 8 style guide.
PEP 8, also known as the Python Enhancement Proposal 8, is a set of coding standards and guidelines for writing 
computer programs in the Python programming language. The following is a summary of the PEP 8 style guide used in this
application:

- **Indentation:** Use of 4 spaces per indentation level.
- **Whitespace:** Use of whitespace to separate elements in the code, such as operators, commas, and semicolons.
- **Naming Conventions:** Use of ```snake_case``` for variables, functions, and methods.
- **Imports:** Imports placed at the top of the file, grouped together, and sorted alphabetically.
- **Strings:** Use of double quotes `````" "````` for string literals.
- **Comments:** Inline comments used with space after the ```#``` symbol and use of ```:``` as a standard PyCharm 
    commenting feature.
- **Code Organization:** Code is grouped into sections as much as possible, with each section separated by a comment 
    line.
---

## Features

- **Random Word Generation:** A random word is selected from a pre-defined word list, ```hangman1_wordList.
  word_list```, using the ```random.choice()``` method.

- **Dyslexic Letter Shuffle:** The selected word is converted to a list, the letters are shuffled using ```random.
   shuffle()``` method and then converted back to a string.

- **Riddle Clue:** A riddle is generated as a clue to the word to be guessed. The code uses a CSV 
  file```hangman1_clue.csv```to search for the randomly generated word, and if a match is found, the corresponding 
  riddle is displayed to the user.

- **Game Play Loop:** The game play loop is implemented using a while loop that continues until the user either 
    correctly guesses the word or runs out of lives. The user is prompted to guess a letter, and the code checks if the 
    letter is in the word. If the letter is in the word, the corresponding underscores are replaced with the letter. If 
    the letter is not in the word, the user loses a life, and the hangman ASCII art is updated.

- **End Game Condition:** The while loop breaks out when either all the letters in the word have been correctly 
   guessed, or the user runs out of lives. In the first case, the user wins, and in the second case, the user loses.

- **ASCII Art:** The code uses ASCII art to represent the hangman stages, which is imported from the hangman1_ascii 
   module.

## Additional Features for Future Development

The here are just some of many examples for additional features that can be added to the game in future development. 
I choose the following features because they will improve the users engagement during game play and make the games code 
more readable and maintainable.

- **Graphical User Interface (GUI):** using Tkinter.

- **Phonics** functionality that will allow the user to guess the word by spelling it out phonetically.

- **Clear screen:** functionality that refreshes the ASCII art after each guess.

- **Save game:** functionality that saves the game state to a file.

- **Word Length:** The game can be made more challenging by adding word length. The user can choose between short, 
   medium, and long words. The short words will have 4 to 6 letters, the medium words will have 7 to 9 letters, and the 
   long words will have 10 or more letters.

- **Word Categories:** The game can be made more challenging by adding word categories. The user can choose between 
   different categories, such as animals, food, and sports. The code will then randomly select a word from the 
   selected category.

- **Try and Except:** Code can be modified to use try and except to handle errors.

- **User defined functions and / or Classes:** A version of the Game made up entirely of user defined functions or 
   Classes to improve code readability and maintainability.

- **Pandas:** Third party library that can be used to read the CSV file or.

- **JSON file:** The code can be modified to use a JSON file to store the words and riddles.

---

## Help Documentation


### Dependencies - But not needed for Game Play:

1. Pip 21.2.4 or later
2. Pytest 6.2.5 or later

### Requirements to Run the Game:

1. Python 3.8 or later (Python 3.11 used for development)
2. Windows 10 or later (+ **Windows Terminal**) or
3. macOS 10.15 or later (+ **Terminal**) or 
4. Linux - Ubuntu 20.04 or later (+ **Terminal**)
5. PyCharm IDE (optional)
6. Visual Studio Code (optional)

### Installation Instructions:

1. Ensure that you have **Python3 installed** on your computer. If you do not have Python3 installed, you can 
   download it from **[here](https://www.python.org/downloads/)**.
2. Download the zip file from the **[<> code ](https://github.com/SkimJazz/CA_T1A3_terminal-app-1)** drop-down box in 
   the GitHub Repository and save it to a directory of your choice (e.g. **Desktop**).
3. Unzip the file.
4. Open Terminal or Windows Terminal and do the following:
    - ```cd``` into the directory  where the file was unzipped. e.g. ```cd desktop\CA_T1A3_terminal-app-1-main```
5. In the Terminal or Windows Terminal, type ```bash run_game.sh``` and press ```Enter```.
6. The game will start. Go to **Game Play Instructions** below for instructions on how to play the game.

### Game play Instructions:

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

---


## Algorithmic Thinking and Logic

> **NOTE:** Algorithmic thinking and Logic is explained in terms of the following sections in the code and not 
> according 
> to the features listed in the Features section above, as some features overlap, and well; it just makes more sense!
> - ===== Dyslexic Letter Shuffle =====
> - ===== Read CSV file =====
> - ===== Game Play Loop =====

<br>

### Dyslexic Letter Shuffle:

The letters in the word to guess are shuffled, making it different from a traditional Hangman Game. This feature was 
added to make the game more challenging, but it also has a practical purpose for dyslexics.

For some people with dyslexia, spelling a word can be difficult. By shuffling the letters in the word, the game makes 
it more challenging for everyone, and it also simulates some of the difficulties that dyslexics face when trying to 
spell words. This feature makes the game both fun and educational, as it helps players understand some of the 
challenges that dyslexics face in their daily lives.

The code follows a straightforward logic and is structured in a way to make it easy to understand and maintain. The 
shuffling feature is implemented in a way that ensures that each time the game is played, a different word will be 
displayed to the user in a shuffled form.

<br>

Here's how the **Dyslexic Letter Shuffle** section works:


- **Random Word Generation:** A word is selected randomly from a pre-defined word list. The list of words is stored 
  in the ```hangman1_wordList.word_list``` module. The function ```random.choice``` is used to select a word from the 
  list.

```python
# : hangman1_main.py -> Randomly select a word from the wordList
gen_word = random.choice(hangman1_wordList.word_list)

# : hangman1_wordList.py -> List of words to be used in the game
word_list = ['eagle', 'penguin', 'wolf']
```

- **Word to List Conversion:** The selected word is converted into a list of individual characters. This step is 
  done to make it easier to shuffle the letters of the word.

```python
# : Convert the randomly generated word to a list
    word_list = list(gen_word)
```

- **Shuffling of Letters:** The random.shuffle function is used to shuffle the letters in the list. This function 
  rearranges the order of the elements in the list randomly.

```python
# : Shuffle letters in the list
    random.shuffle(word_list)
```
- **List to Word Conversion:** The shuffled letters are then converted back to a string by using the join method. The 
  result is stored in the variable shuffled_word.

```python
# : Convert the shuffled letters back to a string
    shuffled_word = "".join(word_list)
```

- **Word Length Calculation:** The length of the shuffled word is calculated and stored in the variable 
  ```word_length```.

```python
# : Get the length of shuffled word
    word_length = len(shuffled_word)
```

- **Initializing the Display Word:** The list ```display_word``` is initialized to store the characters to be displayed
to the user. This list is initialized with a set of underscores that are equal in number to the length of the shuffled 
  word. The underscores represent the missing letters that the user needs to guess.

```python
display_word = []
    for _ in range(word_length):
        display_word += "_"
```

<br>

### Read CSV file:

The Riddle feature in this Dyslexic Hangman Game adds an element of fun and engagement to the game. Instead 
of just guessing the word through trial and error, the player must also solve a riddle to determine the word they are 
trying to guess. This additional layer of challenge can make the game more engaging, as the player must use their 
problem-solving skills to both decipher the riddle and guess the word.

For dyslexic players, this feature can also provide a more accessible way to play the game. Rather than just focusing 
on spelling the word, the player can use their creativity and critical thinking skills to solve the riddle and 
determine the word. This can make the game a more positive and empowering experience for dyslexic players.

The logic behind Read CSV file section is to efficiently search for a word in a CSV file and retrieve the corresponding
riddle. The code handles any errors that may occur during the search and provides clear messages to the user indicating 
the outcome of the search.

<br>

Here's how the **Read CSV file** section works for displaying the riddle:

- **Open the CSV file:** The code uses the ```with``` statement to open the file ```hangman1_clue.csv``` for reading. 
  This ensures that the file will be properly closed after the code within the block is executed.

```python
with open('hangman1_clue.csv', "r") as read_obj:
```

- **Read the contents of the file:** The code uses the ```csv.DictReader``` method to read the contents of the file and 
  store it in the ```reader``` object. The contents of the file are then stored in a list called ```rows```.

```python
    reader = csv.DictReader(read_obj)
    rows = list(reader)
```

- **Initialize variables:** The code initializes the ```match_found``` variable to False and the ```riddle``` variable 
  to an empty string. These variables will be used to keep track of whether a match has been found and to store the 
  corresponding riddle.

```python
    # : Search for word in CSV file
    match_found = False
    
    # : Initialize var to store riddle
    riddle = ""
```

- **Search for the word:** The code uses a for loop to iterate over each row in the ```rows``` list. For each row, the
  code checks if the ```word``` key in the row dictionary matches the ```gen_word``` variable. If a match is found, the 
  code sets the ```match_found``` variable to True and stores the riddle corresponding to the word in the ```riddle``` 
  variable. The loop then breaks, since there is no need to keep searching if a match has been found.

```python
# : Iterate over each row in csv using reader object
        for row in rows:
            # : Check random word matches word in CSV file
            if row['word'] == gen_word:
                match_found = True

                # : Read from CSV file
                riddle = row['riddle']
                break
```

- **Handle the outcome of the search:** The code uses an ```if``` statement to handle the outcome of the search. If a 
  match was found, the code displays the riddle along with a message. If a match was not found, the code displays a 
  message indicating that a match was not found.

```python
# : ERROR handling PASS -> display riddle if match found
        if match_found:
            print("\nHere's a riddle:", "\n")
            print(riddle)
            print("\nwhat am I?")

        # : ERROR handling FAIL -> message if match not found
        else:
            print("Match not found.")
```

<br>

### Game Play Loop:

The Game Play Loop provides a simple and straightforward implementation of a word guess, allowing the user to 
guess letters and updating the display word based on the user's guesses.

The logic behind the algorithm is to provide a basic game play loop that takes a users input, checks for errors and 
win/lose conditions, and updates the game status. The algorithm provides a clear and readable flow of the game's logic,
making it easier to understand and modify the code if needed.

<br>

Here's how the **Game Play Loop** section works:


- **Play loop:** The game play loop starts with a while loop that continues until the end of the game. The end of 
the game is defined by a variable "end_game", which is initially set to False.

```python
while not end_game:
```

- **User guess input:** The code takes the user's guess as an input then converts it to a lowercase using the 
```input()``` function and the ```lower()``` method.

```python
    # : User guess input
    u_guess = input("\nGuess a letter or press 'Zero' and 'Enter' to quit game: ").lower()
```

- **Error handling:** The code checks if the user's guess has already been made by checking if the letter is in the 
```display_word``` list. If the user's guess has already been made, the code prints an error message.

```python
    # : ERROR handling -> already guessed letters
    if u_guess in display_word:
        print("You already guessed that letter")
```

- **Exit game option:** The code then checks if the user entered ```0``` as the input, which is used as an option to 
exit the game. If the input is ```0```, the code breaks out of the ```while not end_game``` loop and the game ends.

```python
    # : EXIT game option -> can't use letters as a break-out condition
    if u_guess == "0":
        print("Yeah Nice! Catch ya next time")
        # end_game = True  # : Not needed
        break
```

- **Check validity of guess:** The code checks if the user's guess is a single letter using the ```isalpha()```
method and checking the length of the input using the ```len()``` function. If the user's guess isn't a single letter, 
the code prints out an error message. I chose the ```isalpha()``` method to check if the input consists of only 
alphabetical characters, since its compatible with Windows, iSO, and Linux.

```python
 # : ERROR handling -> letters only-> 'isalpha()' Linux/iSO compatible method
        if u_guess.isalpha() and len(u_guess) == 1:

        # : Rest of the code goes here ... lines 89 - 131

        else:
            print("Invalid input. Please enter a single letter.")
```

- **Cross-reference guess with word:** If the user's guess is a single letter, the code starts a for loop to 
cross-reference the user's guess with the letters in the word.

```python
        # : Cross-reference letter guess with letters in word
        for letter_position in range(word_length):

            # : Get letter position
            letter = shuffled_word[letter_position]

```

- **Update display word:** If the user's guess is in the word, the corresponding underscore in the ```display_word``` 
list is replaced with the letter. If not, the user loses a life.

```python
        # : If letter in word, replace underscore with letter
            if letter == u_guess:
                display_word[letter_position] = letter

        # : Print the display_word list as a string
        print(" ".join(display_word))

```

- **Check win/lose conditions:** The code checks if there are no more underscores in the ```display_word``` list. If 
there are no more underscores, the user has won the game and the ```end_game``` variable is set to ```True```. If the 
user loses all their lives, the ```end_game``` variable is also set to True. The code prints a message indicating
to the user they have lost the game. The code prints the updated ```display_word``` list, the hangman stage, and the 
win/lose status.

```python
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
```

---










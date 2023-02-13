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
- [Trello](https://trello.com/b/JG1YwlOK/ca-t1a3-terminal-app)
- [Preso Video - YouTube](   )

---

## Tech Stack

- Python 3.11.0 - Programming Language
- Pytest 6.2.5 - Testing **(Check if this is updated version)**
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

## Installation


### Requirements to Run Game:
> NEED TO UPDATE the following

1. Python 3.11.0
2. Pip 21.2.4
3. Pytest 6.2.5
4. Windows 10 or 11, macOS Operating Systems
5. Terminal to install and run the Game


### Installation Instructions:

1. Download the code from the GitHub repository:
2. Open the terminal and navigate to the folder where the code is saved.
3. Run ```pip install -r requirements.txt``` to install the required libraries.
4. Run ```python3 hangman1.py``` to start the game.


---

## Game Play 


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

## Implementation and Management



### Game Play Loop:

- The game play loop is implemented using a while loop that continues until the user either correctly guesses the 
  word or runs out of lives.
> Add Trello img

### Random Word Generation:

- Random word is selected from a pre-defined word list, 
```hangman1_wordList.word_list```, using the ```random.choice()``` method.
> Add Trello img

### End Game Condition:

- The game ends when the user correctly guesses the word or runs out of lives.
- Option to play again or quit game
> Add Trello img

### ASCII Art:

- ASCII art is imported from the hangman1_ascii module.
- ASCII art is displayed at each stage of the game.
- ASCII art is displayed at the end of the game.

> Add Trello img

### Dyslexic Letter Shuffle:

- The selected word is converted to a list, the letters are shuffled using ```random.shuffle()``` method and then 
  converted back to a string.
- The shuffled word is displayed to the user.

> Add Trello img

### Riddle Clue:

- CSV search for word and associated riddle
- CSV search for word and riddle with error handling
- CSV search for word and riddle with error handling and user input

> Add Trello img

### Executable File:

- Executable file created using PyInstaller

> Add Trello img

---

## Algorithmic Thinking and Logic

> **NOTE:** Algorithmic thinking and Logic is explained in terms of the following sections in the code and not 
> according 
> to the features listed in the Features section above, as some features overlap, and well; it just makes more sense!
> - ===== Dyslexic Letter Shuffle =====
> - ===== Read CSV file =====
> - ===== Game Play Loop =====


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

Here's how the **Read CSV file** section works:

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


<br>

---

Here's how the game works:

1. The computer selects a random word from a list of words and shuffles the letters in the word.
2. The player is shown the length of the word as a series of underscores and is asked to guess a letter.
3. If the letter is in the word, the computer replaces the underscores with the correctly guessed letter.
4. If the letter is not in the word, the player loses a "life." The player starts with 6 lives, and the game ends when
   either all the letters have been correctly guessed or the player has used up all of their lives.
5. The computer also displays a riddle that corresponds to the word the player is trying to guess, to provide an 
   additional clue.
6. The player can choose to quit the game at any time by entering "0."

The code uses various techniques and algorithms to make the game work, such as loops and conditionals to control the 
flow of the game and keep track of the player's lives and guesses, and the use of lists and strings to display the 
word and the guessed letters. The game also uses error handling to ensure that the player inputs valid information 
and to give helpful messages if the input is incorrect.


### Code explanation - Iterative Steps

1. Import the required modules: csv, random, hangman1_wordList, and hangman1_ascii. 
2. Define a function play_game to start the game.
3. Display an ASCII art intro and provide information about the game to the user.
4. Choose a word randomly from the word list in hangman1_wordList module.
5. Convert the randomly generated word to a list, shuffle the letters, and then convert it back to a string.
6. Create an empty list display_word to store the letters that have been correctly guessed.
7. Initialize variables for the game such as end_game to indicate whether the game is over, lives to keep track of 
remaining chances, and match_found to keep track of whether the word is found in the csv file. 
8. Open the csv file hangman1_clue.csv using the open function.
9. Use a csv reader object to read the contents of the csv file.
10. Iterate over each row in the csv file and check if the randomly generated word matches the word in the csv file. 
If a match is found, retrieve the riddle from the corresponding row and display it to the user.
11. Start a while loop to run the game until end_game is True.
12. In each iteration of the while loop, get the user's guess of a letter.
13. If the user's input is "0", end the game.
14. If the user's input is a single letter, check if it's in the shuffled word. If it's in the word, replace the 
corresponding underscores in display_word with the letter.
15. If the letter is not in the shuffled word, decrement the lives by 1. If lives reaches 0, end the game and display 
a message "You lose!".
16. If there are no more underscores in display_word, end the game and display a message "You win!".
17. Display the corresponding ASCII art stage based on the number of lives remaining.
18. If the user's input is not a single letter, display an error message "Invalid input. Please enter a single letter."
19. Finally, if the __name__ of the script is __main__, call the play_game function.


- ASCII art intro is printed on the screen.

```python
print("\nHey! Welcome to")
print(intro)
print("\nThis Hangman game has a twist. The letters in the word are shuffled. Good luck!")
```

- A random word is selected from the word_list and shuffled.

```python
gen_word = random.choice(hangman1_wordList.word_list)
word_list = list(gen_word)
random.shuffle(word_list)
shuffled_word = "".join(word_list)
word_length = len(shuffled_word)
```

- The display_word list is initialized with underscores.

```python
display_word = []
for _ in range(word_length):
    display_word += "_"
```
- The hangman1_clue.csv file is opened and read to find the matching word and get its associated riddle.

```python
with open('hangman1_clue.csv', "r") as read_obj:
    reader = csv.DictReader(read_obj)
    rows = list(reader)
    match_found = False
    riddle = ""
    for row in rows:
        if row['word'] == gen_word:
            match_found = True
            riddle = row['riddle']
            break
    if match_found:
        print("\nHere's a riddle:", "\n")
        print(riddle)
        print("\nwhat am I?")
    else:
        print("Match not found.")
```

- The game loop starts where the user is asked to enter a letter guess.

```python
while not end_game:
    u_guess = input("\nGuess a letter or press 'Zero' and 'Enter' to quit game: ").lower()
```

- The entered letter is checked against the display_word list to see if the user has already guessed that letter.

```python
if u_guess in display_word:
    print("You already guessed that letter")
```

- The user has the option to exit the game by entering '0'.

```python
if u_guess == "0":
    print("Yeah Nice! Catch ya next time")
    break
```
- The entered letter is validated to ensure that it's a single letter.

```python
if u_guess.isalpha() and len(u_guess) == 1:
```
- The letter is compared to the letters in the word. If the letter is in the word, the corresponding underscore is 
replaced.

```python
for letter_position in range(word_length):
    letter = shuffled_word[letter_position]
    if letter == u_guess:
        display_word[letter_position] = letter
print(" ".join(display_word))
```

- If the letter is not in the word, a life is lost, and the number of lives is checked. If all lives are lost, the 
game ends, and the user loses.

```python
if u_guess not in gen_word:
    print(f"You guessed {u_guess}, that's not in the word. You lose a life")
    lives -= 1
    if lives == 0:
        end_game = True
        print("You lose!")
```






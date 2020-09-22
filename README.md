# Python 3 Programming Specialization
Exercises and projects made in the Python 3 Programming Specialization offered by the University of Michigan.

Learn more about the specialization here: https://www.coursera.org/specializations/python-3-programming

# Relevant projects


> NOTE: The following projects are just exercises, and they doesn't have any other purpose but to put in practice all the knowledge acquired in the courses.

### Course 5: Python Project: Pillow, Tesseract and OpenCV

**Project consisting in the use of the libraries behind pillow, tesseract, and opencv in python to build a simple search application.**

The program gets an input keyword. Then reads images in zip files with the ZipFile library (each image in the zip file is the page of a newspaper). And finally, it reads all the text in the images and outputs images of faces contained in the images where the keyword is found. The output is a contact sheet made with the PIL library.
In other words, the code allows to search through the images looking for the occurrences of keywords and faces. 
For example: if you search for "pizza" it will return a contact sheet of all the faces which were located on the newspaper page which mentions "pizza".

### Course 4: Python Classes and Inheritance

**Wheel of Fortune game implemented with Python.**

This project is the implementation of a simplified version of the game Wheel of Fortune. This is how the game works:
<br/>
<br/>
There are <em>n</em> human players and <em>n</em> computer players. Every player has some amount of money ($0 at the start of the game) and a set of prizes (none at the start of the game).And the goal is to guess a phrase within a category. 

Players see the category and an obscured version of the phrase where every alphanumeric character in the phrase starts out as hidden (using underscores: _):
```
Category: Artist & Song

Phrase: _______ _______'_ _ ____ ______ ____ ___
```

During their turn, every player spins the wheel to determine a prize amount and ...

##### if the wheel lands on a cash square, players may do one of three actions:

- Guess any letter that hasn’t been guessed by typing a letter (a-z).
  - Vowels (a, e, i, o, u) cost $250 to guess and can’t be guessed if the player doesn’t have enough money. All other letters are “free” to guess.
  
  - The player can guess any letter that hasn’t been guessed and gets that cash amount for every time that letter appears in the phrase.
  
  - If there is a prize, the user also gets that prize (in addition to any prizes they already had).
  
  - If the letter does appear in the phrase, the user keeps their turn. Otherwise, it’s the next player’s turn.
  
    Example: The user lands on $500 and guesses ‘W’. There are three W’s in the phrase, so the player wins $1500.

- Guess the complete phrase by typing a phrase (anything over one character that isn’t ‘pass’)
  - If they are correct, they win the game
  
  - If they are incorrect, it is the next player’s turn

- Pass their turn by entering 'pass'

##### if the wheel lands on “lose a turn”, the player loses their turn and the game moves on to the next player

##### if the wheel lands on “bankrupt”, the player loses their turn and loses their money but they keep all of the prizes they have won so far.

The game continues until the entire phrase is revealed (or one player guesses the complete phrase)


### Course 3: Data Collection and Processing with Python (REST API's)

**The program uses combined data from two different APIs to make movie recommendations (TasteDive and OMDB).**

The TasteDive API lets you provide a movie (or bands, TV shows, etc.) as a query input, and returns a set of related items. The OMDB API lets you provide a movie title as a query input and get back data about the movie, including scores from various review sites (Rotten Tomatoes, IMDB, etc.).

The program use TasteDive to get related movies for a whole list of titles, combines the resulting lists of related movies and sort them according to their Rotten Tomatoes scores (*We get the Rotten Tomatoes scores trough the OMDB API.)


### Python Functions, Files, and Dictionaries - A Sentiment Classifier

**Program to perform a sentiment analysis (with Twitter data in this particular case).**

The program reads through some collected raw Twitter data. Then makes a CSV file to produce a graph of your results and visualize data.


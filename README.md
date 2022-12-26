# Blackjack Game
This is a simple text-based implementation of the card game Blackjack. The game is played with a standard deck of 52 cards, with values of 11 for an Ace, 2-10 for their face value, and 10 for a Jack, Queen, or King.

# Getting started
To start playing the game, clone or download this repository and run the play_game() function in the command line.

# Usage
To play the game, run the play_game() function in the command line. The game will start by dealing two cards to the player and the computer. The player will then be prompted to get more cards or pass until the game is over. The game is over when either the player or the computer has Blackjack, the player has gone over 21, or the player has decided to pass. After the player's turn, the computer will continue to deal cards until its score is at least 17 or it has Blackjack. The final hands and scores of the player and the computer, and the result of the game, will then be displayed in the command line.

# Functions
deal_card(): This function returns a random card from the deck.
calculate_score(): This function takes a list of cards as input and returns the score calculated from those cards.
compare(): This function compares the scores of the player and the computer and returns a string indicating the result of the game.
play_game(): This function implements the game flow for a single game of Blackjack.
Dependencies
This code uses the random and art modules. The art module is used to print the game's logo in the command line.

# Examples
Here is an example of a game of Blackjack:

# Copy code
$ python blackjack.py
  _____
 /      \
/  BLACK  \
\   JACK   /
 \        /
  \_____/

Your cards: [10, 3], current score: 13
Computer's first card: 10
Type 'y' to get another card, or 'n' to pass: y
Your cards: [10, 3, 6], current score: 19
Type 'y' to get another card, or 'n' to pass: n
Your final hand: [10, 3, 6], final score: 19
Computer's final hand: [10, 10, 8], final score: 28
Opponent went over. You win

# Contributing
If you would like to contribute to this project, please fork the repository and create a pull request with your changes.

import random
from art import logo  # import the logo function from the art module

def deal_card():
    """Return a random card from the deck.

    Returns:
        int: the value of the dealt card
    """
    # create a list of all the possible cards in the deck
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # choose a random card from the list
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Takes a list of cards and return the score calculated from the cards.

    Args:
        cards (list of int): the list of cards to calculate the score for

    Returns:
        int: the calculated score
    """
    # check if the player has Blackjack (2 cards with a score of 21)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    # if there is an Ace in the list and the score is over 21, change the Ace's value to 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)  # remove the Ace from the list
        cards.append(1)  # add a 1 to the list to represent the Ace's new value
    
    # return the sum of the cards as the score
    return sum(cards)

def compare(user_score, computer_score):
    """Compares the scores of the player and the computer and returns a string indicating the result of the game.

    Args:
        user_score (int): the player's score
        computer_score (int): the computer's score

    Returns:
        str: the result of the game
    """
    if user_score == computer_score:  # scores are equal
        return "Draw"
    elif computer_score == 0:  # computer has Blackjack
        return "Lose, opponent has Blackjack"
    elif user_score == 0:  # player has Blackjack
        return "Win with a Blackjack"
    elif user_score > 21:  # player went over 21
        return "You went over. You lose"
    elif computer_score > 21:  # computer went over 21
        return "Opponent went over. You win"
    elif user_score > computer_score:  # player has a higher score
        return "You win!"
    else:  # computer has a higher score
        return "You lose"

def play_game():
    """Implements the game flow for a single game of Blackjack."""
    print(logo)  # print the logo
    
    user_cards = []  # create an empty list for the player's cards
    computer_cards = []  # create an empty list for the computer's cards
    is_game_over = False  # flag to determine when the game is over

    # deal 2 cards to the player and the computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # while the game is not over, prompt the player to get more cards or pass
    while not is_game_over:
        
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, or 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()

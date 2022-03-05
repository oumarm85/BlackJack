############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
# computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
cpu_cards = []
cpu_total = 0
player_total = 0
pick_card = True
pick_again = "y"


def player_draw(player_total):
    player_cards.append(random.choice(cards))

    if 11 in player_cards and sum(player_cards) >= 21:
        for item in range(len(player_cards)):
            if player_cards[item] == 11:
                player_cards[item] = 1

    player_total = sum(player_cards)

    return player_total


def cpu_draw(cpu_total):
    if cpu_total <= 17:
        cpu_cards.append(random.choice(cards))

        if 11 in cpu_cards and sum(cpu_cards) >= 21:
            for item in range(len(cpu_cards)):
                if cpu_cards[item] == 11:
                    cpu_cards[item] = 1

        cpu_total = sum(cpu_cards)

    return cpu_total


def compare(player_total, cpu_total):
    if player_total > 21:
        outcome = "You went over 21, You Loose!"
        return outcome
    elif player_total == cpu_total:
        outcome = "It's a draw"
    elif cpu_total > 21:
        outcome = "You Win!"
    elif player_total <= 21:
        if player_total == 21:
            outcome = "Blackjack!! You WON!"
            return outcome
        elif player_total > cpu_total:
            outcome = "You Won!"
        else:
            outcome = "You Loose"

    return outcome


print(art.logo)

for _ in range(2):
    p_score = player_draw(player_total)
    c_score = cpu_draw(cpu_total)

while pick_card == True:
    print(f"Your cards: {player_cards}, giving you a score of: {p_score}")
    print(f"Computer's first card is: {cpu_cards[0]}")
    pick_again = input("Type 'y' to get another card, or 'n' to pass: ").lower()

    if pick_again == "y":
        p_score = player_draw(player_total)

        if p_score > 21:
            c_score = 100
            pick_card = False
            winner = compare(p_score, c_score)
            print(f"Your final hand is: {player_cards}, giving you a final score of: {p_score}")
            print(winner)
        elif p_score == 21:
            compare(p_score, c_score)
            winner = compare(p_score, c_score)
            pick_card = False
            print(f"Your final hand is: {player_cards}, giving you a final score of: {p_score}")
            print(winner)

    elif pick_again == "n":
        pick_card = False
        while c_score < 17:
            c_score = cpu_draw(cpu_total)
        winner = compare(p_score, c_score)
        print(f"Your final hand is: {player_cards}, giving you a final score of: {p_score}")
        print(f"Computer's final hand is: {cpu_cards}, giving a final score {c_score}")
        print(winner)
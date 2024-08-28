# blackjack-game
The provided Python code simulates a basic Blackjack game. Here's a breakdown of its functionality:

1. Card Generation:
The card_generator function randomly selects a card from a deck of 52 cards.
It returns the numerical value of the card, with face cards (Jack, Queen, King) having a value of 10.

3. Player's Turn:
The player is initially dealt two cards.
The player is asked if they want to draw a third card.
The sum of the player's card values is calculated.

4. Dealer's Turn:
The dealer is dealt two cards.
The sum of the dealer's card values is calculated.

5. Outcome Determination:
If the player's sum is 21, they automatically win.
If the player's sum exceeds 21, they lose.
If neither player has a sum of 21, the player with the higher sum wins.
If both player and dealer have the same sum, it's a tie.

Summary:
The code effectively simulates a basic Blackjack game with card generation, player and dealer turns, and outcome determination.

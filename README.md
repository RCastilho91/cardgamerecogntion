# cardgamerecognition
This repository is focused on building a Machine Learning model for recognizing playing cards and other specific needs of card game 'Tranca'.

The goal is to build a recognition algorithm that correctly identifies the cards and sequences (see item 4.1 in the explanatory part below) in a picture, subsequently calling in the scoring algorithm (also included in this repository as contador_tranca.py).

THE GAME OF 'TRANCA'

1. Players

The game can be played between 2 (individually), 3 (individually), 4 (in pairs) or 6 people (in trios).


2. Sets of cards


The game is played with regular sets of cards, excluding Jokers.


A game with up to 4 players will be played with 2 sets of cards. 6 players will require 3 sets of cards.


3. Objectives


The goal of each individual, pair or trio is to sum the greatest amount of points through any given quantity of rounds, ending when they reach at least 3,500 points (up to 4 players) or 5,000 points (6 players).


4. Game structure and strategy


'Tranca' is played by forming sequences of 3 or more cards, equal or subsequent to each other, until the player runs out of cards in their hand. Once a player is out of their first hand, they pick up one of the two available mortos (second set of 11 cards) and continues playing. Once the player depletes their morto, the round is over.


Sequences that are laid out in front of a player count positive points at the end of a round, while the cards in a player's hand count negative points to them. Any sequence a player lays out in front of them must have at least 3 subsequent or equal cards.


If the cards from the stock are depleted, a morto should replace it. If all cards from the stock are depleted and no more mortos are available to replace it, the round is over. An individual or team that does not pick up their morto will have -100 points at the end of the round.


A player that successfully depleted their morto by using the last card in their hand or discarding it will earn +100 points.


The main strategy of the game is to create sequences of 7 or more cards, which are called canastras.


4.1. Canastras

Canastras are point boosters. They are sequences of 7 or more cards of the same suit (excluding any eventual 2s used as jokers, which can be of any suit). Canastras made of the same card are also equally valid, such as 7 Kings (or 6 Kings and a 2).


A canastra that contains a 2 (equivalent to the joker), denominated a dirty canastra, is worth 100 points.


A canastra that was made without any 2's in it, however, denominated a clean canastra, is worth 200 points.


A player cannot deplete their morto and end a round if they have no canastras.


By convention canastras made of the same card are piled vertically, face up, if they are dirty. If they are clean, they are piled horizontally, face up. Note that this convention will be respected in the machine learning algorithm for this project. A pile of cards placed horizontally will be understood as clean canastra, and vertically as dirty canastra.


A canastra made exclusively of 2's is worth 1,000 points. It is strongly recommended that you only try this when playing with 6 players, as it would required obtaining 58% of the available 2's rather than 87.5% in games with 4 or less people.


As a canastra is composed of 7 or more cards, when there are 4 players or less, it is recommended (for game quality purposes) that sequences of a same card are limited to the "edges" (namely 4, 5, King and Ace). Building a canastra would require that you obtain at least 6 of the 8 cards similar available (plus a 2, as joker), making it unlikely for the canastra to be completed and impairing all players' possibilities in making a "horizontal" sequence.


4.2. Dollars

A dollar is a red 3, meaning it could be hearts or diamonds. Each dollar could help or damage a player's score at the end of the round. Dollars are laid separately from the players' sequences. Dollars cannot be used as part if one's sequence (such as 3, 4, 5...).


Any player who has a dollar will need to have a canastra when the round ends. If they have a canastra, each dollar will be worth an extra 100 points each. However, if the player has a dollar but was unable to form a canastra, each dollar will be worth minus 100 points.


4.3. Twos (equivalent to jokers)

As mentioned in topic 4.1, all 2 cards can be used as jokers. That means they can take over the position of any given card in a sequence, limited to 1 in each sequence.


5, 6, 7, 2, 9, 10, J is an example of a valid sequence using a 2 to replace an 8. This is also an example of a dirty canastra, worth 100 points.


4.4. Discard pile

The discard pile may eventually have several useful cards.


A player may collect the discard pile for themselves once their turn starts if, and only if:


The last card discarded fits a sequence already made public by them; or

The last card discarded fits a sequence of at least 2 other cards in their hand.

If a player chooses to collect the discard pile, they must use the last card discarded prior to any other action, and they must also collect all the cards contained in it. They must also discard one of the cards to end their turn regularly.


Discard pile examples:


Player B has a sequence of 7, 8 and 9 of clubs already laid out in front of them. Player A just discarded a 10 of clubs. It is now player B's turn.


Example 1: Player B takes the 10 and builds their 7, 8 and 9 sequence. Player B takes all other cards from the discard pile and discards one to signal the end of their turn once they're done with organizing their hand, building their sequences and laying out new ones if they wish to do so.

Example 2: Player B has a Jack of clubs and a 2 of diamonds in their hand, and they wish to create a new sequence rather than build the one laid out in front of them. Player B uses these two cards to pick up the 10 of clubs and lays the 10, J, 2 sequence separately to the 7, 8, 9 in front of them. Player B takes all other cards from the discard pile and discards one to signal the end of their turn once they're done with organizing their hand, building their sequences and laying out new ones if they wish to do so.
Aside from the above given examples, a player may not pick up from the discard pile.


4.5. Trancas

Black suited 3s (clubs or spades) negatively impact a player's score if they end the round with one in their hands. A tranca is worth -100 points. They cannot be used in any sequences (such as 3, 4, 5...).


They can be strategically used to keep the next player from picking the discard pile, as they cannot be directly picked up for having no direct use.


5. Game setup

Whenever playing with 4 or 6 people, the players should sit in an intermittent fashion to their teammates (meaning a Team A player would be followed by a Team B player, who is followed by a Team A player and so on).


If you're playing in teams, it would be advisable that one player for each team takes responsibility for laying out the sequences being worked on in front of them. These players should preferably be sitting opposing to each other as to maximize playing space.


Once teams are established, a player may volunteer to shuffle and deal the cards.


The player who shuffles the deck will deal 11 cards, face down, to each player.


The player to the right of the one who shuffled will make two more piles of 11 cards each and keep them separated for a later phase of the game. These piles are called morto (or 'dead' (pile) in Portuguese).


All cards that have not been used can now be put in a stock, face down, at arms reach of every player.


Once all players have 11 cards in their hands, the morto is separated and the stock is within players' range, the game is ready to begin.


6. Playing the game

'Tranca' is played clockwise, meaning the first player will be that to the left of the one who shuffled and distributed the main cards.


All players check whether they have any dollars in their hands. If they do, they are to lay out the threes separately and draw a new card from the stock to replace it, respecting the player order. Any player who draws a red 3 from the stock should immediately set it on the table and replace it with the next card on the stock.


A turn starts with a player either drawing a card from the stock, or picking up the discard pile (please see item 4.4.). A player does not have to set out any sequences from their hand if they don't want to (it's strategically recommended when playing individually) unless they pick from the discard pile (if they do, they only have to reveal the sequence they used the first card they picked for). If the game is being played in groups, it is recommended that any sequences of 3 or more cards are revealed so that the teammates can contribute in building them towards a canastra.


A player cannot build a pre-existing sequence to pick another player's discard. During their turn, the player may organize their hand and lay out and/or build existing sequences on their side of the table. A player's turn is over when they discard.


If a player depletes their first hand and discards, they will pick up the morto and wait for their next turn to play normally. If this player uses all of their first hand cards and does not discard, they pick up the morto and continues playing immediately until they discard.


Once a player ends their turn, the player to their left will start theirs. The round will be over and scoring made once the morto is depleted, either by a player using it or by it replacing the regular stock (once it's depleted). Each player or team has right to only one morto. If they deplete a morto, the round will be over.


Once the round is over, the player to start will now shuffle and deal the main cards and will be the last to play. The player to their right will deal the morto.


7. Scoring

Cards laid out in front of the players will count positively, while the ones in their hands will count negatively towards the score.


Point boosters and penalties:


Clean canastra (+200 points): sequences of 7 equal or subsequent cards without any 2s being used as jokers.

Dirty canastra (+100 points): sequences of 6 equal or subsequent cards complemented with a 2 being used as jokers.

Twos canastra (+1,000 points): sequences of 7 or more 2 cards.

Dollars (+100/-100 points): red 3 cards accumulated during the round. They will be worth +100 points if player/team managed to build a canastra of any kind, and -100 points if not.

Morto (0/-100 points): if the individual or team picked up and used the morto during the round, they will not be discounted anything. Otherwise, -100 points to the round score will have to be considered.

Trancas (-100 points): a player may eventually finish the round without having been able to discard them. -100 points each.

Final move (+100 points): if a player manages to make the last move in a round, discarding or using their last card and there is no more morto to get acquired, the player or team will be awarded an extra 100 points.


Counting cards:


Aces: are worth +15 points each;

Eight through King: are worth +10 points each;

Four through Seven: are worth +5 points each;

Two: are worth +10 points each;

Dollars: the card themselves are worth +5 points, even if no canastra was built to generate its booster effect;


The final score will be the sum of the boosters and the sequences laid out in front of a player/team, minus what they have on their hands.


Once a player or team manages to hit the scoring specified in section 3. Objectives, the game is over and won by that player/team.

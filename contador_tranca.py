def handValue(hand,gotMorto):
    """
    This function will register and count what a player (or team) has on their hands that will impact the score negatively.
        - hand: is expected to be a single list containing all the individual cards player(s) had on their hands;
        - gotMorto: boolean expression indicating whether the player or team have advanced to the second phase by picking up
        the second available pile denominated morto.
        
    This function returns the total sum of the cards on a players hand plus any boosters.
    
    """
    
    # establishing counters and sum variables.
    # tranca, as a counter, is being declared for future player leaderboard and statistics
    totalSubtract = 0
    tranca = 0
    trancaSum = 0
    regularSubtract = 0
    
    # analyzes whether got morto will have an actual impact on the final scoring
    if gotMorto == True:
        mortoImpact = 0
    else:
        mortoImpact = -100
    
    # loop to analyze a player's hand
    for card in hand:
        if cardDict[card]['Tranca'] == True:
            tranca += 1
        else:
            regularSubtract -= cardDict[card]['Value']
    
    # generating total sums
    trancaSum = tranca * -100
    totalSubtract = trancaSum + regularSubtract + mortoImpact
    
    # returning results
    print("")
    print("Negative factors: ")
    print("")
    print("Hand value: " + str(regularSubtract))
    print("Trancas: " + str(tranca) + " ("+ str(trancaSum) + ")")
    if mortoImpact == -100:
        print("Morto: " + str(mortoImpact))
    print("")
    print("Total negative impact: " + str(totalSubtract))
    print("")
    print("--------------------------------")
    
    return totalSubtract

def tableValue(sequences,finalMove):
    """
    
    This function registers all values that count positively towards a player or teams score.
        - sequences: receives a list of lists that contain each sequence a player has laid out in front of them
        - finalMove: boolean expression that indicates whether the player or team has made the final move of the game
        thus being awarded an extra 100 points.
    
    """
    
    # establishing sum variables for displaying scoring boosters
    dirtyCanastraBooster = 0
    cleanCanastraBooster = 0
    dollarBooster = 0
    finalMoveBooster = 0
    totalTable = 0
    jokerCanastra = 0
    
    # establishing counters for effect multipliers
    dirtyCanastra = 0
    cleanCanastra = 0
    dollar = 0
    joker = 0
    
    # checking all sequences built for value and boosters
    for sequence in sequences:
        
        # summing the individual card values outside the boosters established above
        for card in sequence:
            totalTable += cardDict[card]['Value']
            # Checking whether the current card is a dollar (red 3)
            if cardDict[card]['Dollar'] == True:
                dollar += 1
            # Checking whether the current card is a joker (2)
            if cardDict[card]['Joker'] == True:
                joker += 1
            
        # Checking whether the sequence is a canastra
        if len(sequence) >= 7:
            # Checking whether the sequence is composed by jokers (2) only
            # if so, the booster is assigned and a dirty canastra is removed from the counter
            if joker == len(sequence):
                jokerCanastra = 1000
            # Checking whether there are any jokers at all to assign to dirty or clean canastra counters
            elif joker > 0:
                dirtyCanastra += 1
            else:
                cleanCanastra += 1
    
    # removing a canastra counter if there is a joker canastra in the game
    if jokerCanastra == 1000:
        dirtyCanastra -= 1
        
    # accounting for the boosters
    dirtyCanastraBooster = 100 * dirtyCanastra
    cleanCanastraBooster = 200 * cleanCanastra
    dollarBooster = 100 * dollar
    totalCanastra = dirtyCanastra + cleanCanastra
    
    # checking whether the dollar will have negative effect
    if dollar > 0 and totalCanastra == 0:
        dollarBooster = dollarBooster * -1
    
    # checking whether the player has the final move booster
    if finalMove == True:
        finalMoveBooster = 100
    
    # returning the results
    print("Positive factors: ")
    print("")
    print("Total dirty canastras: " + str(dirtyCanastra) + " | Total value: " + str(dirtyCanastraBooster))
    print("Total clean canastras: " + str(cleanCanastra) + " | Total value: " + str(cleanCanastraBooster))
    print("Total dollars: " + str(dollar) + " | Total value: " + str(dollarBooster))
    print("Table value: " + str(totalTable))
    if finalMove == True:
        print("Final move booster: " + str(finalMoveBooster))
    if jokerCanastra > 0:
        print("Joker canastra booster: " + str(jokerCanastra))
    print("")
    finalPositiveScoring = totalTable + dirtyCanastraBooster + cleanCanastraBooster + dollarBooster + finalMoveBooster + jokerCanastra
    print("Total positive scoring: " + str(finalPositiveScoring))
    print("")
    print("--------------------------------")
    
    return finalPositiveScoring
    
def scoreRound(finalHand,gotMorto,finalTable,finalMove):
    """
    This function runs the final score of a player or team's round.
        - finalHand: is expected to be a single list containing all the individual cards player(s) had on their hands;
        - gotMorto: boolean expression indicating whether the player or team have advanced to the second phase by picking up
        the second available pile denominated morto.
        - finalTable: receives a list of lists that contain each sequence a player has laid out in front of them
        - finalMove: boolean expression that indicates whether the player or team has made the final move of the game
        thus being awarded an extra 100 points.
    """
    
    print("")
    # calling both functions established above
    finalScoring = tableValue(finalTable,finalMove) + handValue(finalHand,gotMorto)
    #returning the value
    print("Final round scoring: " + str(finalScoring))
    
# establishing a list of jokers
jokers = ['two_hearts','two_clubs','two_spades','two_diamonds']

# establishing lists of cards by value standards
fifteenPoints = ['ace']
tenPoints = ['eight','nine','ten','jack','queen','king']
fivePoints = ['four','five','six','seven']

# establishing the regular cards and suits to build a dictionary
allCards = ['two','three','four','five','six','seven','eight','nine','ten',
            'jack','queen','king','ace']
suits = ['clubs','spades','hearts','diamonds']

# establishing card ordering for future validation of whether a given sequence is valid

cardOrder = {
    'four': 1,
    'five': 2,
    'six': 3,
    'seven': 4,
    'eight': 5,
    'nine': 6,
    'ten': 7,
    'jack': 8,
    'queen': 9,
    'king': 10,
    'ace': 11
}

# establishing a dictionary of all cards with their name, suits, value, order and boolean checks
card = ""
cardDict = {card:{}}

# updating dictionary for future reference
for suit in suits:
    for card in allCards:
        
        mask = card + "_" + suit
        # Analyzing cards of value three, which can have multiple effects
        if card == 'three':
            if suit == 'clubs' or suit == 'spades':
                cardDict.update({mask:{
                    'Name': card,
                    'Suit': suit,
                    'Value': -100,
                    'Tranca': True,
                    'Dollar': False,
                    'Joker': False,
                    'Order': None
                }})
            else:
                cardDict.update({mask:{
                    'Name': card,
                    'Suit': suit,
                    'Value': 5,
                    'Tranca': False,
                    'Dollar': True,
                    'Joker': False,
                    'Order': None
                }})
        
        # Analyzing jokers
        if card == 'two':
            cardDict.update({mask:{
                'Name': card,
                'Suit': suit,
                'Value': 10,
                'Tranca': False,
                'Dollar': False,
                'Joker': True,
                'Order': None
            }})
            
        # Analyzing cards of value five
        if card in fivePoints:
            cardDict.update({mask:{
                'Name': card,
                'Suit': suit,
                'Value': 5,
                'Tranca': False,
                'Dollar': False,
                'Joker': False,
                'Order': cardOrder[card]
            }})
            
        # Analyzing cards of value ten
        if card in tenPoints:
            cardDict.update({mask:{
                'Name': card,
                'Suit': suit,
                'Value': 10,
                'Tranca': False,
                'Dollar': False,
                'Joker': False,
                'Order': cardOrder[card]
            }})
        
        # analyzing ace, which is valued at 15
        if card == 'ace':
            cardDict.update({mask:{
                'Name': card,
                'Suit': suit,
                'Value': 15,
                'Tranca': False,
                'Dollar': False,
                'Joker': False,
                'Order': 11
            }})
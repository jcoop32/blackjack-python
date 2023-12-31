import random
#  Black Jack
#  Rules:
#  When the dealer has served every player, the dealers face-down card is turned up. 
#  If the total is 17 or more, it must stand. If the total is 16 or under, they must take a 
#  card. The dealer must continue to take cards until the total is 17 or more, at which point 
#  the dealer must stand.

#  Goal- Beat the Dealer or get 21

#  deck of cards:
#  4 of each
#  [ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king]
    # -ace can be used as a 1 or 11.
    # -face cards are all worth 10

# 1. computer and player need to be 'drawn' 2 random cards
# 2. ask if user wants to 'hit' or 'stay'
    # - if 'hit' 'draw' a new card
        # -once the amount is over 21 they automatically loose
    # - if 'stay' they keep the current amount and computer reveals amount
        # -if computer amount <= 16 they must draw until they have >= 17
# 3. Decide winner
    # if user amount is <=21 and > computer amount -> user wins
    # if user amount is >21 -> computer automatically wins
    # if computer amount === user amount draw


# ace card-
# if player or dealer pulls an ace, it is an 11 unless it will make their total > 21, which will turn it into a 1
# future features:
# - add bank account
# - double your money if you win
# - check past game logs

exitGame = False

cards = [11, 11, 11, 11, 2, 2, 2, 2, 3, 3, 
3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7,
7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
10, 10, 10, 10, 10]


class Player():
    attr = {
        "total": 0,
        "gamesWon": 0,
    }

user = Player()
dealer = Player()

def startGame():
    user.attr['total'] = 0
    dealer.attr['total'] = 0
    userCards = cards[random.randint(0, len(cards) - 1)]
    dealerCards = cards[random.randint(0, len(cards) - 1)]
    for i in range(0, 4):
        if (i == 0):
            print('User Card #' + str(i + 1) + ': ' + str(userCards))
            user.attr['total'] = user.attr['total'] + userCards
        if (i == 1):
            print('User Card #' + str(i + 1) + ': ' + str(userCards))
            user.attr['total'] = user.attr['total'] + userCards
        if (i == 2):
            print('Dealer Card #' + str(i + 1) + ': ' + str(dealerCards))
        if (i == 3):
            print('Dealer Card #' + str(i + 1) + ': Hidden')        
    

startGame()
# Blackjack game
# Making the Player class
from random import randint
playerHand = 0
dealerHand = 0
class Player(object):
    # Making a bankroll and a hand
    def __init__(self, bankroll, hand):
        self.bankroll = bankroll
        self.hand = hand

    def addBankroll(self, amount):
        self.bankroll += amount
    def subtractBankroll(self, amount):
        self.bankroll -= amount
    def setHand(self, hand):
        self.hand = playerHand




# Making the Dealer class
class Dealer(object):
    # Making a bankroll
    def __init__(self, bankroll, hand):
        self.bankroll = bankroll
        self.hand = hand

    def addBankroll(self, amount):
        self.bankroll += amount

    def subtractBankroll(self, amount):
        self.bankroll -= amount
#     Saving the hand
    def setHand(self):
        self.hand = dealerHand

# Making the hand of the Player
player = Player(bankroll=100, hand = 0)
dealer = Dealer(bankroll=100, hand=0)


# Deal function
def deal(playerHand, dealerHand):
    value1 = randint(1, 10)
    playerHand += value1
    value1 = randint(1, 10)
    playerHand += value1
    value1 = randint(1, 10)
    dealerHand += value1
    value1 = randint(1, 10)
    dealerHand += value1
    player.hand = playerHand
    dealer.hand = dealerHand

def hit(playerHand):
    value1 = randint(1, 11)
    player.hand += value1
    if(dealer.hand <= 17):
        value1 = randint(1, 11)
        dealer.hand += value1


def stand(playerHand):
    value1 = 0
    playerHand += value1
    player.hand += playerHand




# Playing the game
while(True):
    # Basic game setup
    if(player.bankroll == 0):
        print("Buddy, your bankrupt!")
        print("You have $0 to bet!")
        print("Go ask ur parents for more money to bet")
        exit(0)
    print("Welcome to Blackjack!")
    print("Money you have: $%s" % player.bankroll)
    print("Money that the dealer has: $%s" % dealer.bankroll)
    # Asking player for how much he/she wants to beg
    betAmount = input("How much are you willing to bet? ")
    print("Bet amount: $%s" % betAmount)
    betAmount = int(betAmount)
    player.subtractBankroll(int(betAmount))
    deal(playerHand, dealerHand)
    print("Your hand: %s" %player.hand)
    choice = input("Type h to hit or s to stand ")
    if(choice.lower() == 'h'):
        hit(player.hand)
        if (player.hand == 21 or dealer.hand > 21):
            print("Congratulations! You win!")
            print("Your hand: %s" % player.hand)
            print("Dealer's hand: %s" %dealer.hand)
            print("You won $%s" %betAmount)
            player.addBankroll(betAmount*2)
            dealer.subtractBankroll(betAmount)
            playAgain = input("Would you like to play again?")
            if (playAgain[0].lower() == "y"):
                continue
            elif (playAgain[0].lower() == "n"):
                exit(0)
        elif (player.hand > 21 or player.hand > 21 and dealer.hand > 21):
            print("Busted! Your value is above 21")
            print("Your hand: %s" % player.hand)
            print("Dealer's hand: %s" % dealer.hand)
            print("You lost $%s" % betAmount)
            dealer.addBankroll(betAmount)
            playAgain = input("Would you like to play again?")
            if (playAgain[0].lower() == "y"):
                continue
            elif (playAgain[0].lower() == "n"):
                exit(0)
    elif(choice.lower() == 's'):
        stand(playerHand)
    print("Your hand: %s" %player.hand)
    choice = input("Type h to hit or s to stand ")
    if(choice.lower() == 'h'):
        hit(player.hand)
    elif(choice.lower() == 's'):
        stand(playerHand)

    if(player.hand > dealer.hand and player.hand < 21 or dealer.hand > 21):
        print("Congratulations! You win!")
        print("You won $%s" % betAmount)
        player.addBankroll(betAmount*2)
        dealer.subtractBankroll(betAmount)
        print("Your hand: %s" % player.hand)
        print("Dealer's hand: %s" % dealer.hand)
        playAgain = input("Would you like to play again?")
        if (playAgain[0].lower() == "y"):
            continue
        elif (playAgain[0].lower() == "n"):
            exit(0)
    elif(player.hand < dealer.hand):
        print("Oof! The dealer had a better hand!")
        print("Your hand: %s" % player.hand)
        print("Dealer's hand: %s" % dealer.hand)
        print("You lost $%s" % betAmount)
        dealer.addBankroll(betAmount)
        playAgain = input("Would you like to play again?")
        if (playAgain[0].lower() == "y"):
            continue
        elif (playAgain[0].lower() == "n"):
            exit(0)
    elif(player.hand > 21):
        print("Busted! Your hand is larger than 21")
        print("Your hand: %s" % player.hand)
        print("Dealer's hand: %s" % dealer.hand)
        print("You lost $%s" % betAmount)
        dealer.addBankroll(betAmount)
        playAgain = input("Would you like to play again?")
        if (playAgain[0].lower() == "y"):
            continue
        elif (playAgain[0].lower() == "n"):
            exit(0)
    elif(player.hand == dealer.hand):
        print("Tie! Both your hands were equal")
        player.bankroll += betAmount
        playAgain = input("Would you like to play again?")
        if (playAgain[0].lower() == "y"):
            continue
        elif (playAgain[0].lower() == "n"):
            exit(0)

    player.hand = 0
    dealer.hand = 0
    playAgain = input("Would you like to play again?")
    if (playAgain[0].lower() == "y"):
        continue
    elif (playAgain[0].lower() == "n"):
        exit(0)

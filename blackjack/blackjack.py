"""

7th July 2022 - Ideas

Aims:
    
    Play Blackjack
    Add bet
    Calculate Winnings
    Store Balance

Additional Features:

    Store Balance Across Games

Notes:

    52 Cards
    Deal 2 Cards to the player and dealer

"""

import pandas as pd
import random

cards = pd.DataFrame({
    'Card' : ["2H","3H","4H","5H","6H","7H","8H","9H","10H","JackH","QueenH","KingH","AceH","2D","3D","4D","5D","6D","7D","8D","9D","10D","JackD","QueenD","KingD","AceD","2C","3C","4C","5C","6C","7C","8C","9C","10C","JackC","QueenC","KingC","AceC","2S","3S","4S","5S","6S","7S","8S","9S","10S","JackS","QueenS","KingS","AceS"],
    'Value' : [2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11]
    })

def deal(handarr):
    for i in range(2):
        rand = random.randint(0,51)
        handarr.loc[len(handarr.index)] = [cards.loc[rand,'Card'], cards.loc[rand,'Value']]

def hit(handarr):
    rand = random.randint(0,51)
    handarr.loc[len(handarr.index)] = [cards.loc[rand,'Card'], cards.loc[rand,'Value']]

def value(handarr):
    handval = 0
    for x in handarr.index:
        handval = handval + handarr.loc[x,'Value']
    return handval


play = input("Would you like to play? Y/N\n").upper()

while play == "Y":

    print("\n" * 25)

    playerVal = 0
    dealerVal = 0
    hitQ = "Y"
    Bust = False

    playerHand = pd.DataFrame({
        'Card': [],
        'Value': []
        })

    dealerHand = pd.DataFrame({
        'Card': [],
        'Value': []
        })

    deal(playerHand)
    playerVal = value(playerHand)
    for x in playerHand.index:
        print("Players", x, "card is",playerHand.loc[x,'Card'])
    print("Players current hand value is", playerVal)
    print("\n")
    deal(dealerHand)
    dealerVal = value(dealerHand)
    for x in dealerHand.index:
        print("Dealers", x, "card is", dealerHand.loc[x,'Card'])
    print("Dealers current hand value is", dealerVal)

    #Check for BlackJacks
    if playerVal == 21 and dealerVal == 21:
        print("Draw, take bets back")
    elif playerVal == 21:
        print("Player Wins!")
    elif dealerVal == 21:
        print("Dealer Wins!")

    while hitQ == "Y":
        hitQ = input("Would you like to hit? Y/N\n").upper()
        if hitQ == "N":
            print("Players final hand value is", playerVal)
            break
        else:
            hit(playerHand)
            playerVal = value(playerHand)
            print("Players current hand value is", playerVal)
            if playerVal > 21:
                print("Player is bust. Player Loses...")
                Bust = True
                break

    if Bust == False:
        #Dealer must hit until 17 or more value
        while dealerVal < 17:
            hit(dealerHand)
            dealerVal = value(dealerHand)
        
        print("Dealers final hand value is", dealerVal)

        #Win Conditions
        if playerVal == 21 and dealerVal == 21:
            print("Draw, take bets back")
        elif playerVal < 21 and playerVal == dealerVal:
            print("Draw, take bets back")
        elif playerVal > 21 and dealerVal > 21:
            print("Both bust. Draw, take bets back")
        elif dealerVal > 21 and playerVal < 21:
            print("Player Wins!")
        elif playerVal > dealerVal and playerVal <=21:
            print("Player Wins!")
        elif playerVal < dealerVal and dealerVal <=21:
            print("Dealer Wins!")
        elif playerVal > 21:
            print("Dealer Wins!")
        else:
            print("Problem...")

    play = input("Would you like to play again? Y/N")

print("Closing...")
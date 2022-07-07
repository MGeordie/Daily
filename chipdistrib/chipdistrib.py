"""
24 June 2022 - ChipDistribution

Aims:

    Allow chip value range customisations
    Ask the user to enter a $ amount
    Convert the $ into poker chips for texas hold'em
    Return the chip distribution

Additional Features:

    Track Players Balance
    Check profit for/against for the night


Notes:

    - 3 different buy in levels:

        $10 - 20bb
        $25 - 50bb
        $50 - 100bb


    Each player should have 50 chips to start with.

    Lowest 2 chip values should cover 3/5 of the 50 Big-Blinds.

    Chip Conversion Charts ($10 Buy-in / BigBlind 50c):
    
        Printed |Value($)           |Quantity       |Ratio      |Amount
        5       |       0.05        |       0       |   0       |   0.00
        10      |       0.10        |       0       |   0       |   0.00
        25      |       0.25        |       20      |   20      |   5.00
        50      |       0.50        |       8       |   16      |   4.00
        100     |       1.00        |       1       |   4       |   1.00
        500     |       5.00        |       0       |   0       |   0.00
        1000    |       10.00       |       0       |   0       |   0.00
    
    Chip Conversion Charts ($25 Buy-in / BigBlind 50c):

        Printed |Value($)           |Quantity       |Ratio      |Amount
        5       |       0.05        |       0       |   0       |   0.00
        10      |       0.10        |       0       |   0       |   0.00
        25      |       0.25        |       20      |   20      |   5.00
        50      |       0.50        |       20      |   40      |   10.00
        100     |       1.00        |       10      |   40      |   10.00
        500     |       5.00        |       0       |   0       |   0.00
        1000    |       10.00       |       0       |   0       |   0.00

    Chip Conversion Charts ($50 Buy-in / BigBlind 50c):
    
        Printed |Value($)           |Quantity       |Ratio      |Amount
        5       |       0.05        |       0       |   0       |   0.00
        10      |       0.10        |       0       |   0       |   0.00
        25      |       0.25        |       40      |   40      |   10.00
        50      |       0.50        |       40      |   80      |   20.00
        100     |       1.00        |       15      |   60      |   15.00
        500     |       5.00        |       1       |   20      |   5.00
        1000    |       10.00       |       0       |   0       |   0.00

        Formula:
            Where SB and BB are your Small Blind / Big Blind Chips. Xup is just 1 colour up
            EG: .50c buy in, you need this formula total value of chips in the BB colour
            
            SB = ((Buyin * 0.6) * 0.33) rounded to nearest chip value
            BB = ((Buyin * 0.6) * 0.66) rounded to nearest chip value
            1up = (Buyin * 0.35)rounded
            2up = (Buyin * 0.05)rounded

        Test Case:
            40 Buyin
            SB = 7.92 rounded to 8
            BB = 15.84 rounded to 16
            1up = 14
            2up = 2 left over but isn't enough so shifted down

            
            



    Menu:

        1. Adjust Value Table
        2. Adjust Big Blind
        3. Track Stats
        4. Buy-in
        5. Quit

"""
#Imports
import logging
import numpy as np
import pandas as pd

#Default Values (To be changed to read from file)
bigBlind = 0.50
smallBlind = 0.25
currBuyin = 0
option = 9
lastTotal = 0
withdrawSesh = 0
buyinSesh = 0
totalSesh = 0

payout = pd.DataFrame({
    'Colour': [],
    'Value': [],
    'Ratio': []
})

balances = pd.read_csv('stats.csv')
values = pd.read_csv('values.csv')

def x_round(x,y):
    return round(x*y)/y

def menu():
    print("What would you like to do?")
    print("1) Buy-in")
    print("2) Withdraw")
    print("3) Adjust Chip Values and Colours")
    print("4) Adjust Blinds. Currently set(Big Blind / Small Blind):", bigBlind, " ", smallBlind)
    print("5) View Current Stats/Totals")
    print("0) Validate and End Session")

def stats():
    print(balances)
    print("What would you like to do?")
    print("1) Add new player")
    print("2) Check Player Stats")
    print("3) Check Logs")
    print("0) Return")

#Grabbing the current Pot Value
for x in balances.index:
    lastTotal = lastTotal + balances.loc[x,'Balance']

logging.basicConfig(filename='action.log', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
logging.debug('----------Starting Session----------')

while option == 9:

    print("\n" * 10)
    menu()
    option = int(input())

    #Buy-in and Chip Distribution
    while option == 1:
        logging.info('---BuyIn Started---')
        output = pd.DataFrame({
            'Colour': [],
            'Amount': [],
            'Value': []
        })

        print("\n" * 10)
        playerCheck = input("Who is buying in?\n")
        validName = False
        for x in balances.index:
            if playerCheck == balances.loc[x,'Name']:
                validName = True
                playerRow = x
        if validName == False: 
            print("Player not found, please add player first. Returning to main menu...")
            logging.info('%s attempted to buy-in with their name but has not created a user.', playerCheck)
            logging.info('---BuyIn Ended---')
            option = 9
            break
        currBuyin = int(input("How much would you like to buy-in with?\n"))
        logging.info('%s has attempted to buy-in with %d', playerCheck, currBuyin)
        trackBuy = currBuyin
        payoutcount = 0
        outputCount = 0
        for x in values.index:
            if values.loc[x,'Value'] >= smallBlind:
                payout.loc[payoutcount] = [values.loc[x,'Colour'], values.loc[x,'Value'],values.loc[x,'Ratio']]
                payoutcount += 1
        for x in payout.index:
            if trackBuy >= payout.loc[x,'Value']:
                temp = x_round(currBuyin * payout.loc[x,'Ratio'],(1/payout.loc[x,'Value']))
                amount = temp / payout.loc[x,'Value']
                value = amount * payout.loc[x,'Value']
                output.loc[outputCount] = [payout.loc[x,'Colour'], amount, value]
                trackBuy = trackBuy - temp
                outputCount += 1
            else:
                for x in reversed(payout.index):
                    if trackBuy >= payout.loc[x,'Value'] and trackBuy != 0:
                        temp = x_round(trackBuy,(1/payout.loc[x,'Value']))
                        trackBuy = trackBuy - temp
                        output.loc[x,'Amount'] = output.loc[x,'Amount'] + 1
                        output.loc[x,'Value'] = output.loc[x,'Amount'] * payout.loc[x,'Value']
        
        balances.loc[playerRow,'Balance'] = balances.loc[playerRow,'Balance'] + currBuyin
        balances.loc[playerRow,'Buyin'] = balances.loc[playerRow,'Buyin'] + currBuyin
        print("Added $", currBuyin, "to " + playerCheck +"'s balance. Their balance is now",balances.loc[playerRow,'Balance'])
        print(output)
        logging.info('%.2f has been added to %s balance. Their balance is now %.2f', currBuyin, playerCheck, balances.loc[playerRow,'Balance'])
        logging.info('---BuyIn Ended---')
        option = 9

    #Withdraw
    while option == 2:
        logging.info('---Withdraw Started---')
        print("\n" * 10)
        playerCheck = input("Who is withdrawing?\n")
        validName = False
        for x in balances.index:
            if playerCheck == balances.loc[x,'Name']:
                validName = True
                playerRow = x
        if validName == False: 
            print("Player not found, please add player first. Returning to main menu...")
            logging.info('%s attempted to withdraw with their name but has not created a user.', playerCheck)
            logging.info('---Withdraw Ended---')
            option = 9
            break
        currWithdraw = int(input("How much would you like to withdraw? AVAILABLE BALANCE:$%.2f \n" % balances.loc[playerRow,'Balance']))
        logging.info('%s has attempted to withdraw $%.2f from their balance of $%.2f', playerCheck, currWithdraw, balances.loc[playerRow,'Balance'])
        if currWithdraw <= balances.loc[playerRow,'Balance']:
            logging.info('Valid Withdrawal, begining process')
            balances.loc[playerRow,'Balance'] = balances.loc[playerRow,'Balance'] - currWithdraw
            print('You have successfully withdrawn $', currWithdraw, ". You now have $", balances.loc[playerRow,'Balance'], " remaining.")
            logging.info('Withdrawal Successful. %s has withdrawn $%.2f and their new balance is $%.2f',playerCheck,currWithdraw,balances.loc[playerRow,'Balance'])
            balances.loc[playerRow,'Withdraw'] = balances.loc[playerRow,'Withdraw'] + currWithdraw
            option = 9
            logging.info('---Withdraw Ended---')
            break
        else:
            logging.info("Invalid Withdrawal, Not enough in Balance")
            print("You have attempted to withdraw more than your current balance. Returning to main menu...")
            option = 9
            logging.info('---Withdraw Ended---')
            break
        


    #Adjusting Values and Colours of Chips
    while option == 3:
        logging.info('---Adjust Chips Started---')
        print("\n" * 10)
        print(values)
        targetrow = input("What row would you like to adjust? Type 'cancel' to return\n").lower()
        while targetrow.isnumeric() == False:
                if targetrow == "cancel":
                    logging.info('User has cancelled adjusting chips')
                    logging.info('---Adjust Chips Ended---')
                    option = 9
                    break
                targetrow = input("Please enter a row number or type 'cancel' to return:\n")
        else:
            targetcol = input("Which column would you like to update? (Enter column name)\n")
            targetcol = targetcol.title()
            while (targetcol in values.columns) == False:
                targetcol = input("Please enter a valid column...\n")
                targetcol = targetcol.title()
            updatetableval = input("What would you like the new value to be?\n")
            values.loc[targetrow,targetcol] = updatetableval
            logging.info('The %s chip has had the %s updated to %s', values.loc[targetrow,'Colour'], targetcol, updatetableval)
        values.to_csv('values.csv', index=False)
        logging.info('Saving new chip values to values.csv')
        logging.info('---Adjust Chips Ended---')
        option = 9

    #Adjust Big Blind
    while option == 4:
        print("\n" * 10)
        print("This feature is currently not implemented. Returning to menu... \n")
        option = 9
        
        
    #Player Stats and Editing
    while option == 5:
        statoption = 9
        while statoption == 9:
            print("\n" * 10)
            stats()
            print("\n")
            statoption = int(input())
        while statoption == 1:
            dupeName = False
            print("\n" * 10)
            print("What is the new players first name?")
            newfName = input()
            print("What is " + newfName +"'s last name?")
            newlName = input()
            #Check if players name is already in balances table. If so, request new names and pray their name isn't common.
            for x in balances.index:
                if newfName == balances.loc[x,'Name'] and newlName == balances.loc[x,'Surname']:
                    print("Duplicate player detected. If there is going to be two players with the same name, ask Geordie to fix the app as he wasn't expecting someone with a common name to use his program. Cheers for the extra work " + newfName + " " + newlName)
                    dupeName = True
            if dupeName == False:
                balances.loc[len(balances.index)] = [newfName, newlName, 0, 0, 0]
            balances.to_csv('stats.csv', index=False)
            statoption = 9
    #Check Player Stats
        while statoption == 2:
            print("Work in Progress")
            statoption = 9
    #Check Logs
        while statoption == 3:
            print("Work in Progress")
            statoption = 9
        while statoption == 0:
            statoption = 9
            option = 9


    #Validate and End Session
    while option == 0:
        
        for x in balances.index:
            withdrawSesh = withdrawSesh + balances.loc[x,'Withdraw']
            buyinSesh = buyinSesh + balances.loc[x,'Buyin']
            totalSesh = totalSesh + balances.loc[x,'Balance']

        if lastTotal == totalSesh - buyinSesh + withdrawSesh:
            print("All is valid. Saving session...")
            for x in balances.index:
                balances.loc[x,'Withdraw'] = 0
                balances.loc[x,'Buyin'] = 0
            balances.to_csv('stats.csv', index=False)
        else:
            print("Someone done messed up, check log file for who messed up")
            logging.error(balances)

        print("Closing...")
        logging.debug('----------Ending Session----------')
        exit()
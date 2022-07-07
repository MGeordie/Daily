"""

5th July 2022 - Ideas

Aims:
    Able to enter app ideas and store them in a file
    Randomly Pull an Idea
    Mark Complete and link file path
    Add notes to the idea

Additional Features:

    Create Enviroment and file structure upon random generation
    Allow people to submit ideas from web
    Add Checklist
    Gui

Notes:

"""

#Imports
import pandas as pd
import logging
import tkinter as tk
import numpy as np

#Variables
menuOp = 0
running = True
contTag = True

#Ideas Database
ideas = pd.read_csv('ideas.csv')

searchResult = pd.DataFrame({
    'Idea': [],
    'Desc': [],
    'Priority': [],
    'Tag1' : [],
    'Tag2' : [],
    'Tag3' : []
})

def menu():
    print("1)Add a new Idea")
    print("2)Search for an Idea")
    print("3)Randomly Pull an Idea")
    print("4)View my Idea History")
    print("0)Close")

def searchMenu():
    print("1)Priority")
    print("2)Tag")
    print("3)Request-Type")
    print("0)Return to Main-Menu")

logging.basicConfig(filename='action.log', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
logging.debug('----------Starting----------')

while running == True:
    
    menu()
    menuOp = int(input("What would you like to do?\n"))

    #Adding an Idea
    while menuOp == 1:
        logging.info('---Starting Idea Creation---')
        newIdea = input("What is the idea?\n")
        newDesc = input("Please provide a short description:\n")
        newPriority = input("What priority is this idea? (Low/Medium/High)\n")
        newTag1 = input("Enter the first tag:\n")
        newTag2 = input("Enter the second tag:\n")
        requestType = input("Enter the request type: (Self-Request / Submitted\n")            
            
        ideas.loc[len(ideas.index)] = [newIdea, newDesc, newPriority, newTag1, newTag2, requestType]
        logging.info('Added %s to the database', newIdea)

        loopQ = input("Would you like to add another idea? (Y/N)").upper()
        if loopQ == "N":
            searchMenuOp = 9
            logging.info('---Ending Idea Creation---')
    
    #Search for Idea
    while menuOp == 2:
        logging.info('---Starting Search---')
        searchMenuOp = 9
        while searchMenuOp == 9:
            searchMenu()
            searchMenuOp = int(input("How would you like to search?\n"))
        while searchMenuOp == 1:
            logging.info('User attempting Priority Search')
            searchTerm = input("What priority would you like to search? (Low/Med/High)\n")
            results = ideas[ideas['Priority'].str.contains(searchTerm)]
            if results.empty:
                logging.info('Unsuccessful Search. Search term used %s', searchTerm)
                searchTerm = input("No results found...")
                break
            else:
                logging.info('Successful Search. Search term used %s', searchTerm)
                print(results)
            loopQ = input("Would you like to perform another priority search? (Y/N)").upper()
            if loopQ == "N":
                searchMenuOp = 9
                logging.info('Priortiy Search Ended')
        while searchMenuOp == 2:

            #Needs Work
            print("WIP")

            logging.info('User attempting Tag Search')
            searchTerm = input("Enter a tag to be searched?\n")
            for x in ideas.index:
                if ideas.loc[x,'Tag1'] == searchTerm or ideas.loc[x,'Tag2'] == searchTerm:
                    print("No")
            results = ideas[ideas[['Tag1' + 'Tag2']].str.contains(searchTerm)]
            print(results)
            if results.empty:
                logging.info('Unsuccessful Search. Search term used %s', searchTerm)
                searchTerm = input("No results found...")
                break
            else:
                logging.info('Successful Search. Search term used %s', searchTerm)
                print(results)
            loopQ = input("Would you like to search for a different tag? (Y/N)\n").upper()
            if loopQ == "N":
                searchMenuOp = 9
            logging.info('Tag Search Ended')
        while searchMenuOp == 3:
            logging.info('User attempting Request-Type Search')
            searchTerm = input("What request-type would you like to search? (Self-Request/Submitted)")
            results = ideas[ideas['Request-Type'].str.contains(searchTerm)]
            if results.empty:
                logging.info('Unsuccessful Search. Search term used %s', searchTerm)
                searchTerm = input("No results found...")
                break
            else:
                logging.info('Successful Search. Search term used %s', searchTerm)
                print(results)
            loopQ = input("Would you like to perform another request-type search? (Y/N)").upper()
            if loopQ == "N":
                searchMenuOp = 9
                logging.info('Request-Type Search Ended')
        while searchMenuOp == 0:
            logging.info('User Returning to Main Menu')
            logging.info('---Ending Search---')
            break
        break
    
    #Randomly Pull an Idea
    while menuOp == 3:
        logging.info('---Starting Random Idea Generator---')
        print("Generating a random idea...")
        rand = ideas.sample(n=1)
        print(rand)
        logging.info('---Ending Random Idea Generator---')
    
    #View Idea History
    while menuOp == 4:
        logging.info('---Starting Progress Calendar---')
        print("WIP")
        logging.info('---Ending Progress Calendar----')
    
    #Close Program
    while menuOp == 0:
        logging.info('---Starting Close Procedure---')
        running = False
        logging.info('---Ending Close Procedure---')
        break
logging.debug('----------Ending----------')
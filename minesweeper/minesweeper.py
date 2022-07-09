"""

8th - 9th July 2022 - Minesweeper

Aims:
    
    Minesweeper GUI
    Difficulties

Additional Features:

    Stats Saving

Notes:

    Gen an array

  0 | 1 | 2 | 3 | 4 | 5 | 6 |
-----------------------------
  1 |   |   |   |   |   |   |
-----------------------------
  2 |   |   |   |   |   |   |
-----------------------------
  3 |   |   |   |   |   |   |
-----------------------------
  4 |   |   |   |   |   |   |
-----------------------------
  5 |   |   |   |   |   |   |
-----------------------------
  6 |   |   |   |   |   |   |
-----------------------------

    x = rand.randint(0,6)
    y = rand.randint(0,6)

"""

#Imports
from curses import window
import tkinter as tk
import pandas as pd
import random
from array import *

#Variables
mineField = pd.DataFrame()
checkedMine = pd.DataFrame({
    'Row' : [],
    'Column' : [],
    'Value' : [],
    'MineCount' : []
})
buttonDict = {}
mineClose = 0
play = True
# mineCount = 0

def genMines(difficulty):
    if difficulty == "Easy":
        print("Easy mines being generated...")
        for i in range(0,5):
            for y in range(0,5):
                mineRand = random.randint(0,10)
                if mineRand > 2:
                    print("Made it to safe at",i,y)
                    mineField.at[i,y] = "Safe"
                else:
                    print("Made it to Mine at",i,y)
                    mineField.at[i,y] = "Mine"
    elif difficulty == "Medium":
        print("Medium mines being generated...")
        for i in range(0,10):
            for y in range(0,10):
                mineRand = random.randint(0,10)
                if mineRand > 1:
                    print("Made it to safe at",i,y)
                    mineField.at[i,y] = "Safe"
                else:
                    print("Made it to Mine at",i,y)
                    mineField.at[i,y] = "Mine"
    elif difficulty =="Hard":
        print("Hard mines being generated...")
        for i in range(0,20):
            for y in range(0,20):
                mineRand = random.randint(0,10)
                if mineRand > 1:
                    print("Made it to safe at",i,y)
                    mineField.at[i,y] = "Safe"
                else:
                    print("Made it to Mine at",i,y)
                    mineField.at[i,y] = "Mine"
    elif difficulty == "Test":
        print("Easy mines being generated...")
        for i in range(0,5):
            for y in range(0,5):
                mineRand = random.randint(0,10)
                if mineRand > 1:
                    print("Made it to safe at",i,y)
                    mineField.at[i,y] = "Safe"
                else:
                    print("Made it to Mine at",i,y)
                    mineField.at[i,y] = "Mine"
    else:
        print("Problem with difficulty...")
    return mineField

def checkMine(q,x,y):
    if mineField.loc[x,y] == "Mine":
        print("Boom")
        buttonDict[q].config(text="Boom")
        buttonDict[q].config(state="disabled")
    elif mineField.loc[x,y] =="Safe":
        print("Safe")
        mineClose = checkSurround(x,y)
        if mineClose == 0:
            check8(checkedMine,q)
        buttonDict[q].config(text = mineClose)
        buttonDict[q].config(state="disabled")
    else:
        print("Something wrong in checkMine")

#Detects the surrounding 8 squares and checks for mines.
#If a mine is detected, add 1 to the mineClose counter and return the number to be printed on the selected spot.
def checkSurround(x,y):

    #Defines the Search Limits
    minRowRange = 0
    maxRowRange = 3
    minColRange = 0
    maxColRange = 3

    #Mine Counter
    mineClose = 0

    #Sets the pointer to start at the top left square to selected
    row = x-1
    col = y-1

    #Check if at an edge. If so reduce, the search limit so it doesn't try searching outside of the mineField array.
    if x-1 < 0:
        minRowRange = 1
        print("At the top")
    if y-1 < 0:
        minColRange = 1
        print("At the left edge")
    if x+1 > len(mineField)-1:
        maxRowRange = 2
        print("At the bottom")
    if y+1 > len(mineField.columns)-1:
        maxColRange = 2
        print("At the right edge")

    #Loop through search parameters via reading top left to bottom right.
    for i in range(minRowRange,maxRowRange):
        row = x - 1
        row = row + i
        col = y-1
        for a in range(minColRange,maxColRange):
            col = col + a
            if mineField.loc[row,col] == "Mine":
                mineClose = mineClose + 1
                checkedMine.loc[len(checkedMine.index)] = [row,col,"Mine",0]
            else:
                checkedMine.loc[len(checkedMine.index)] = [row,col,"Safe",0]
            col = y-1
    return mineClose

def check8(array,q):
        for b in array.index:
            if array.loc[b,'Value'] == "Safe":

                minRowRange = 0
                maxRowRange = 3
                minColRange = 0
                maxColRange = 3

                if len(mineField) == 5:
                    jumps = [-6,-5,-4,-1,0,1,4,5,6]
                elif len(mineField) == 10:
                    jumps = [-11,-1,9]
                elif len(mineField) == 20:
                    jumps = [-21,-1,19]

                #Set x and y
                x = array.loc[b,'Row']
                y = array.loc[b,'Column']
                print("Checking tile:", x,",",y)

                #Mine Counter
                mineClose = 0

                #Sets the pointer to start at the top left square to selected
                row = x-1
                col = y-1

                #Check if at an edge. If so reduce, the search limit so it doesn't try searching outside of the mineField array.
                if x-1 < 0:
                    minRowRange = 1
                    print("At the top")
                if y-1 < 0:
                    minColRange = 1
                    print("At the left edge")
                if x+1 > len(mineField)-1:
                    maxRowRange = 2
                    print("At the bottom")
                if y+1 > len(mineField.columns)-1:
                    maxColRange = 2
                    print("At the right edge")

                #Loop through search parameters via reading top left to bottom right.
                for i in range(minRowRange,maxRowRange):
                    row = x - 1
                    row = row + i
                    col = y-1
                    for a in range(minColRange,maxColRange):
                        col = col + a
                        if mineField.loc[row,col] == "Mine":
                            mineClose = mineClose + 1
                            array.loc[b,'MineCount'] = mineClose
                        else:
                            array.loc[b,'MineCount'] = mineClose
                        col = y-1
            print("mines found:", mineClose)
            print("Updating")
            pos = jumps[b]
            buttonDict[q+pos].config(text = mineClose)
            buttonDict[q+pos].config(state="disabled")
                        
        array = array.drop(array.index, inplace=True)

#Generate Game Window
def genGame(mineField):
    window = tk.Tk()
    window.geometry("800x1000")
    window.title("Minesweeper")
    i=0
    for x in mineField:
        for y in mineField:
            buttonName = tk.Button(window, text="", command = lambda n=i, row=x ,column=y: checkMine(n,row,column))
            buttonName.config(height=3,width=3)
            buttonName.grid(row=x,column=y,sticky="NSEW")
            buttonDict[i] = buttonName
            i=i+1

    lbl = tk.Label(window,text=("Mines Remaining:"))
    window.mainloop()

difficulty = input("What difficulty would you like?")


while play == True:
    play = True
    genMines(difficulty)
    print(mineField)
    genGame(mineField)
    break

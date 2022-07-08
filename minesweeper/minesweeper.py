"""

8th July 2022 - Minesweeper

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
import tkinter as tk
import pandas as pd
import random

#Variables
mineField = pd.DataFrame()
buttonDict = {}
mineClose = 0
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
    elif difficulty =="Hard":
        print("Hard mines being generated...")
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
        mineClose = checkSurround(q,x,y)
        buttonDict[q].config(text = mineClose)
        buttonDict[q].config(state="disabled")
    else:
        print("Something wrong in checkMine")

def checkSurround(q,x,y):
    minRowRange = 0
    maxRowRange = 3
    minColRange = 0
    maxColRange = 3
    mineClose = 0

    print(x,y)
    print(len(mineField))
    print(len(mineField.columns))

    row = x-1
    col = y-1
    #Check Border
    if x-1 < 0:
        minRowRange = 1
        print("At the top")
    if y-1 < 0:
        minColRange = 1
        print("At the left edge")
    if x+1 > len(mineField) - 1:
        maxRowRange = 2
        print("At the bottom")
    if y+1 > len(mineField.columns) -1:
        maxColRange = 2
        print("At the right edge")

    for i in range(minRowRange,maxRowRange):
        row = x - 1
        row = row + i
        col = y-1
        for a in range(minColRange,maxColRange):
            col = col + a
            if mineField.loc[row,col] == "Mine":
                mineClose = mineClose + 1
            col = y-1
    return mineClose



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
genMines(difficulty)
print(mineField)
genGame(mineField)

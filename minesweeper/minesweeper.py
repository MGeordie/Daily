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

#Generate Window
# window = tk.Tk()
# window.title("Minesweeper")
# window = tk.Label(text="Tkinter is cool.", width=80, height=25)
# window.pack()
# window.mainloop()

def genMines(difficulty):
    if difficulty == "Easy":
        mineCount = 0
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
                    mineCount =+ 1
    elif difficulty == "Medium":
        print("Medium mines being generated...")
    elif difficulty =="Hard":
        print("Hard mines being generated...")
    else:
        print("Problem with difficulty...")
    return mineField

def checkMine(test,x,y):
    if mineField.loc[x,y] == "Mine":
        print("Boom")
    elif mineField.loc[x,y] =="Safe":
        print("Safe")
        test = "X"
    else:
        print("Something wrong in checkMine")


def genGame(mineField):
    window = tk.Tk()
    test= "O"
    for x in mineField:
        for y in mineField:
            tk.Button(textvariable=test, command = lambda row=x ,column=y: checkMine(test,row,column)).grid(row=x,column=y,sticky="ew")
    window.mainloop()

difficulty = input("What difficulty would you like?")
genMines(difficulty)
print(mineField)
genGame(mineField)

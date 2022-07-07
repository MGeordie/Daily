"""
23 June 2022 - Quiz

Aims:

    Ask 6 multiple choice questions
    Pull questions from random out of 12 questions
    Calculate score based on percentage

Additional Features:

    Looping
    Imported Libraries
    Unique Virtual Environment

COMPLETED
"""

import numpy as np
import random

repeat = "Y"

questions = np.array([
["What is 50x2?\n","a)100\n","b)25\n","c)200\n","a"],
["How many fingers does a human have?\n", "a)5\n", "b)10\n", "c)20\n", "b"],
["This question has how many correct answers?\n", "a)3\n", "b)1\n", "c)2\n", "b"],
["What is 9+10*20?\n", "a)190\n", "b)199\n", "c)209\n", "c"],
["What is 1+2*5?\n", "a)15\n", "b)11\n", "c)9\n", "b"],
["'That is _____ car' Fill the blank with the correct grammatical word\n", "a)their\n", "b)there\n", "c)they're\n", "a"],
["What is the closest planet to Earth an average?\n", "a)Mercury\n", "b)Mars\n", "c)Venus\n", "a"],
["How many months in a year?\n", "a)11\n", "b)12\n", "c)10\n", "b"],
["How many days in March?\n", "a)31\n", "b)30\n", "c)29\n", "a"],
["How many grams are in 100ml of water?\n", "a)10g\n", "b)50g\n", "c)100g\n", "c"],
["How bored did Geordie get writing these questions?\n", "a)Very\n", "b)Very x2\n", "c)Very x3\n", "a"],
["What language is this program written in?\n", "a)Python\n", "b)Cobra\n", "c)Viper\n", "a"],
["How many seconds in a day?\n", "a)14440\n", "b)86400\n", "c)72220\n", "b"]])

closeApp = input("Welcome to the quiz! This quiz will contain 6 randomly selected multiple choice questions. Ready to begin? (Y/N)\n")
closeApp = closeApp.upper()
if closeApp == "N":
    print("Closing the quiz...")
    exit()

while repeat == "Y":
    score = 0

    questionsnums = random.sample(range(0,11),6)

    print(questionsnums)

    for x in questionsnums:

        print(questions[x][0] + "\n", questions[x][1] + "\n", questions[x][2] + "\n", questions[x][3] + "\n",)
        answer = input("Enter your answer:\n")
        answer = answer.lower()
        if answer == questions[x][4]:
            score += 1
        
    percent = score / 6 * 100
    print("You scored ", score, " out of 6 questions or ",percent, "\n")

    repeat = input("Would you like to go again?")
    repeat = repeat[0].upper()
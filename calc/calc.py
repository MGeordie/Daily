"""
22 June 2022 - Calculator

Aims:

    Accept 2 inputs, an operation and print out

Additional Features:

    Checking for valid inputs
    Looping until closure requested

COMPLETED
"""

#Variables & Accepting Inputs

running = "Y"

while running == "Y":

    opCheck = False

    fnum = int(input("What is your first number?\n"))
    snum = int(input("What is your second number?\n"))

    while opCheck == False:

        operator = input("What operator would you like to use?\n")

        if operator == "+":
            total = fnum + snum
            opCheck = True
        elif operator == "-":
            total = fnum - snum
            opCheck = True
        elif operator == "*":
            total = fnum * snum
            opCheck = True
        elif operator == "/":
            total = fnum / snum
            opCheck = True
        else:
            print("You have not provided a valid operator, please enter an operator?\n")
            
    else:
        print("\n", fnum, " " , operator, " ", snum, " = ", total, "\n")
        running = input("Would you like to make another calculation? (Y/N)\n")
        running = running.upper()
        while running != "Y" and running != "N":
            running = input("That is not a valid input. Please select Y/N\n")
            running = running.upper()

else:
    print("Closing the Calculator...")
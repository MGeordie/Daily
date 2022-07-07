"""

m = int(input("Enter a number to be ratio'd:"))
a = int(input("Enter the first ratio number:"))
b = int(input("Enter the second ratio number:"))
c = int(input("Enter a third ratio number:"))
d = int(input("Enter a fourth ratio number:"))

fnum = a / (a + b + c + d) * m
snum = b / (a + b + c + d) * m
tnum = c / (a + b + c + d) * m
num4 = d / (a + b + c + d) * m

"""

number = int(input("What number would you like to divide?"))
ratio1 = int(input("Ratio 1:"))
ratio2 = int(input("Ratio 2:"))
ratio3 = int(input("Ratio 3:"))
ratio4 = int(input("Ratio 4:"))

total = ratio1 + ratio2 + ratio3 + ratio4
part = 0.25

print(part)

r1 = ratio1 * part
r2 = ratio2 * part
r3 = ratio3 * part
r4 = ratio4 * part



print(r1, " ", r2, " ", r3, " ", r4)

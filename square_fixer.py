from sys import exit
from math import sqrt


# Read A variable
try:
    getal1 = float(input('A  '))
except ValueError:
    print ("Het is geen getalletje")
    exit()
    
# Read B variable
try:
    getal2 = float(input('B  '))
except ValueError:
    print ("Het is geen getalletje")
    exit()

# Read C variable
try:
    getal3 = float(input('C  '))
except ValueError:
    print ("Het is geen getalletje")
    exit()


if (getal2**2 - 4*getal1*getal3 < 0):
    print ("No solutions")
elif getal1 == 0:
    print ("1 solution")
    print (-getal3/getal2)
else:
    print ("2 solutions")
    sol1 = (-getal2 + sqrt(getal2**2 - 4*getal1*getal3))/(2*getal1)
    sol2 = (-getal2 - sqrt(getal2**2 - 4*getal1*getal3))/(2*getal1)
    
    print (sol1)
    print (sol2)


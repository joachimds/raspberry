import sys



try:
    getal1 = int(input('getal1  '))
except ValueError:
    print ("Het is geen getalletje")
    sys.exit()
    
try:
    getal2 = int(input('getal2  '))
except ValueError:
    print ("Het is geen getalletje")
    sys.exit()

som = int(input('som van de 2 ?'))

if (som == getal1 + getal2):
    print ("slimneus")
else:
    print ("dommerik, het moet {} zijn".format(getal1+getal2))
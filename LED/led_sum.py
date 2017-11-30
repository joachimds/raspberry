import sys
from gpiozero import LED
from time import sleep

greenpin = 26
redpin = 13
orangepin = 19

greentime = 5
redtime = 5
orangetime = 5

green = LED(greenpin)
orange = LED(orangepin)
red = LED(redpin)


try:
    getal1 = int(input('getal1  '))
except ValueError:
    print ("Het is geen getalletje")
    orange.on()
    sleep(orangetime)
    sys.exit()
    
try:
    getal2 = int(input('getal2  '))
except ValueError:
    print ("Het is geen getalletje")
    orange.on()
    sleep(orangetime)
    sys.exit()

som = int(input('som van de 2 ?'))

if (som == getal1 + getal2):
    print ("slimneus")
    green.on()
    sleep(greentime)
else:
    print ("dommerik, het moet {} zijn".format(getal1+getal2))
    red.on()
    sleep(redtime)

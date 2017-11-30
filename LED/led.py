from gpiozero import LED
from time import sleep

greenpin = 26
redpin = 13
orangepin = 19

greentime = 10
orangetime = 2
redtime = 10


green = LED(greenpin)
red = LED(redpin)
orange = LED(orangepin)

while True:
    green.on()
    sleep(greentime)
    green.off()
    orange.on()
    sleep(orangetime)
    orange.off()
    red.on()
    sleep(redtime)
    red.off()





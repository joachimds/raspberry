from gpiozero import LED, Button
from time import sleep
from signal import pause

greenpin = 26
orangepin = 19
redpin = 13
buttonpin = 2

greentime = 10
orangetime = 2
redtime = 10

delaytime = 5

green = LED(greenpin)
orange = LED(orangepin)
red = LED(redpin)
button = Button(buttonpin)

while True:
    
    red.on()
    button.wait_for_press()
    sleep(delaytime)
    red.off()
    green.on()
    sleep(greentime)
    green.off()
    orange.on()
    sleep(orangetime)
    orange.off()
    red.on()
    sleep(redtime)
    red.off()


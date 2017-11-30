from gpiozero import LED, Button
from time import sleep
from signal import pause

greenpin = 26
redpin = 13
buttonpin = 2


green = LED(greenpin)
red = LED(redpin)
button = Button(buttonpin)

while True:
    button.when_pressed = green.on
    button.when_released = red.on


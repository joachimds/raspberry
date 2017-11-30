from gpiozero import LED, Button
from time import sleep

greenpin = 26
buttonpin = 2

greentime = 0.5

green = LED(greenpin)
button = Button(buttonpin)

while True:

    button.wait_for_press()
    green.toggle()
    sleep(greentime)

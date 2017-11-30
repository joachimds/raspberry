from gpiozero import LED, Button, Buzzer
from time import sleep
from signal import pause

greenpin = 26
orangepin = 19
redpin = 13
buttonpin = 2
buzzerpin = 20

greentime = 5
orangetime = 1
redtime = 5

delaytime = 2

green = LED(greenpin)
orange = LED(orangepin)
red = LED(redpin)
button = Button(buttonpin)
buzzer = Buzzer(buzzerpin)

while True:
    red.on()
    button.wait_for_press()
    buzzer.beep()
    buzzer.beep()
    buzzer.off()
    sleep(delaytime)
    red.off()
    green.on()
    buzzer.on()
    sleep(greentime)
    buzzer.off()
    green.off()
    orange.on()
    sleep(orangetime)
    buzzer.beep()
    buzzer.beep()
    buzzer.off()
    orange.off()
    red.on()
    sleep(redtime)
    red.off()


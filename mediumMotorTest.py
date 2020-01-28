from ev3dev2.motor import MediumMotor, OUTPUT_A
from ev3dev2.sound import Sound
from ev3dev2.button import Button
import time

medMot = MediumMotor(OUTPUT_A)
medMot.stop_action = 'hold'
mySnd = Sound()

medMot.on_to_position(30, 0)

mySnd.speak("looking left and right")
medMot.on_to_position(10, 90)
time.sleep(0.5)
medMot.on_to_position(10, -90)
time.sleep(0.5)
medMot.on_to_position(10, 0)

mySnd.speak("spinning")
medMot.on_for_seconds(80, 1)

medMot.on_to_position(50, 0)
mySnd.speak("fixed turn")
for i in range(12):
    medMot.on_for_degrees(30, 30)
    time.sleep(1.0)
medMot.stop()

bttn = Button()
mySnd.speak("Turns until button pressed")

medMot.on(-20)
while True:
    if bttn.enter == 1:
        break
medMot.stop()


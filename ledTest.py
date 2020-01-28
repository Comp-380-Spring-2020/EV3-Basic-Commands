from ev3dev2.led import Leds
import time

leds = Leds()
leds.all_off()
time.sleep(0.5)
leds.set_color('RIGHT', 'GREEN')
for i in range(6):
    amb = i / 6
    leds.set_color('LEFT', (amb, 1.0))
    time.sleep(0.5)

time.sleep(1.0)
leds.all_off()


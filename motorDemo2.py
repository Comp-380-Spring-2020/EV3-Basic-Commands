
from ev3dev2.sound import Sound
from ev3dev2.motor import MoveSteering
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D

rob = MoveSteering(OUTPUT_D, OUTPUT_B)
mySnd = Sound()

mySnd.speak("Turning right in place")
rob.on_for_seconds(50, -50, 2)

mySnd.speak("Spiraling")

rob.on_for_seconds(20, 50, 2)
rob.off()


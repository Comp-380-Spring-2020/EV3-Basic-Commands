
from ev3dev2.sound import Sound
from ev3dev2.motor import LargeMotor, MoveTank, MoveSteering
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D


tank = MoveTank(OUTPUT_D, OUTPUT_B)
mySnd = Sound()


print("turn in place")
mySnd.speak("Turning left in place")

tank.on_for_seconds(-90, 90, 2)


print("curve left")
mySnd.speak("Curving left")
tank.on_for_seconds(45, 80, 2)

print("curve right")
mySnd.speak("Curving right")
tank.on_for_seconds(80, 45, 2)

tank.off()


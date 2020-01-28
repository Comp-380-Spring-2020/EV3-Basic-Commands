
from ev3dev2.sound import Sound

mySnd = Sound()
mySnd.beep()
mySnd.speak("Hello, World!")
mySnd.beep()

# mySnd.play_tone(440, 1.5, 0)
mySnd.tone([(440, 500, 0), (880, 1500, 0)])


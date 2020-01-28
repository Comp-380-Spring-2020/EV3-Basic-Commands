from ev3dev2.button import Button

bttn = Button()
while True:
    print("message")
    if bttn.enter == 1:
        break



from microbit import *

while True:
    gesture = accelerometer.current_gesture()
    if gesture == "face up":
        display.show(Image.HAPPY)
    elif gesture == "shake":
        display.show(Image.ALL_CLOCKS, loop=True, delay=25)
    else:
        display.show(Image.ANGRY)
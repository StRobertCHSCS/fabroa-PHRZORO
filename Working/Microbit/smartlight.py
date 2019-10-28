from microbit import *
import music 
#pins
PIR_pin = pin1
LED_pin = pin0
buzzer = pin2
 
tune = ['f4:4', 'g4:4', 'c4:2', 'g4:3', 'a4:4', 'c4:2','b3:2', 'a4:2', 'f4:2']
while True:
    # if PIR Sensor detects motion, turn on LED
    if PIR_pin.read_digital(): 
        LED_pin.write_digital(1)
        music.play(tune, pin = buzzer)
    else:
        LED_pin.write_digital(0)
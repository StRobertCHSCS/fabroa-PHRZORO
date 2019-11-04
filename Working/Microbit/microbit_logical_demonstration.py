'''
-------------------------------------------------------------------------------
Name: microbit_logical_demonstration_assignment.py

Purpose: When button is pressed while potentiometer is turned down, displays an 
image on the screen while flashing the red led and playing a note on buzzer. 
When button is pressed and potentiometer is turned up, displays an different 
image on the screen while flashing the red led and playing the same note in a 
different octave. If nothing is pressed, red led is turned off and image is 
displayed on screen. 

Authors: Ma.Charlie, Lui.Andrew 	

Created: 03/11/2019 
------------------------------------------------------------------------------
'''
#import microbit module to control microbit, 
#import music module to control sound 
from microbit import *
import music
# name variables, setup pins
crash_sensor = pin2
buzzer = pin15
ad_keypad = pin0
potentiometer = pin1
red_led = pin16
# crash sensor setup 
crash_sensor.set_pull(crash_sensor.PULL_UP)

while True:
    # if button a is pressed while potentiometer is turned down display 
    # happy face, flash red led and play note c on the 4th octave 
    if (ad_keypad.read_analog() > 0 and ad_keypad.read_analog() < 20
            and potentiometer.read_analog() > 0
            and potentiometer.read_analog() <= 511):
        display.show(Image.HAPPY)
        red_led.write_digital(1)
        music.play("c4:2", pin=buzzer)
    # if button b is pressed while potentiometer is turned down display
    # happy face, flash red led and play note d on the 4th octave 
    if (ad_keypad.read_analog() > 40 and ad_keypad.read_analog() < 60
            and potentiometer.read_analog() > 0
            and potentiometer.read_analog() <= 511):
        display.show(Image.HAPPY)
        red_led.write_digital(1)
        music.play("d4:2", pin=buzzer)
    # if button c is pressed while potentiometer is turned down display
    # happy face, flash red led and play note e on the 4th octave
    if (ad_keypad.read_analog() > 90 and ad_keypad.read_analog() < 100
            and potentiometer.read_analog() > 0
            and potentiometer.read_analog() <= 511):
        display.show(Image.HAPPY)
        red_led.write_digital(1)
        music.play("e4:2", pin=buzzer)
    # if button d is pressed while potentiometer is turned down display
    # happy face, flash red led and play note e on the 4th octave
    if (ad_keypad.read_analog() > 130 and ad_keypad.read_analog() < 150
            and potentiometer.read_analog() > 0
            and potentiometer.read_analog() <= 511):
        display.show(Image.HAPPY)
        red_led.write_digital(1)
        music.play("f4:2", pin=buzzer)
    # if button e is pressed while potentiometer is turned down display
    # happy face, flash red led and play note f on the 4th octave
    if (ad_keypad.read_analog() > 500 and ad_keypad.read_analog() < 550
            and potentiometer.read_analog() > 0
            and potentiometer.read_analog() <= 511):
        display.show(Image.HAPPY)
        red_led.write_digital(1)
        music.play("g4:2", pin=buzzer)
    # if crash sensor is pressed display angry face, flash red led
    # and play funk melody 
    if crash_sensor.read_digital() == 0:
        display.show(Image.ANGRY)
        red_led.write_digital(1)
        music.play(music.FUNK, pin=buzzer)
    # if button a is pressed while potentiometer is turned up display
    # surprised face, flash red led and play note c on the 3rd octave
    elif (ad_keypad.read_analog() > 0 and ad_keypad.read_analog() < 20
            and potentiometer.read_analog() > 511
            and potentiometer.read_analog() <= 1023):
        display.show(Image.SURPRISED)
        red_led.write_digital(1)
        music.play("c3:2", pin=buzzer)
    # if button b is pressed while potentiometer is turned up display
    # surprised face, flash red led and play note d on the 3rd octave
    elif (ad_keypad.read_analog() > 40 and ad_keypad.read_analog() < 60
            and potentiometer.read_analog() > 511
            and potentiometer.read_analog() <= 1023):
        display.show(Image.SURPRISED)
        red_led.write_digital(1)
        music.play("d3:2", pin=buzzer)
    # if button c is pressed while potentiometer is turned up display
    # surprised face, flash red led and play note e on the 3rd octave
    elif (ad_keypad.read_analog() > 90 and ad_keypad.read_analog() < 100
            and potentiometer.read_analog() > 511
            and potentiometer.read_analog() <= 1023):
        display.show(Image.SURPRISED)
        red_led.write_digital(1)
        music.play("e3:2", pin=buzzer)
    # if button d is pressed while potentiometer is turned up display
    # surprised face, flash red led and play note f on the 3rd octave
    elif (ad_keypad.read_analog() > 135 and ad_keypad.read_analog() < 140
            and potentiometer.read_analog() > 511
            and potentiometer.read_analog() <= 1023):
        display.show(Image.SURPRISED)
        red_led.write_digital(1)
        music.play("f3:2", pin=buzzer)
    # if button e is pressed while potentiometer is turned up display
    # surprised face, flash red led and play note g on the 3rd octave
    elif (ad_keypad.read_analog() > 535 and ad_keypad.read_analog() < 545
            and potentiometer.read_analog() > 511
            and potentiometer.read_analog() <= 1023):
        display.show(Image.SURPRISED)
        red_led.write_digital(1)
        music.play("g3:2", pin=buzzer)
    # if nothing is done turn off red led and display music note 
    else:
        red_led.write_digital(0)
        display.show(Image.MUSIC_QUAVER)









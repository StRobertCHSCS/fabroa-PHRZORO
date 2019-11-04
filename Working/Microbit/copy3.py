from microbit import *
import music
ad_keypad = pin1
buzzer = pin0
potentiometer = pin5
red_led = pin15
while True:
    if ad_keypad.read_analog() > 0 and ad_keypad.read_analog() < 10 and potentiometer.read_analog() > 0 and potentiometer.read_analog() <= 511:
        # display.show(all_line_1_beam, delay = 125)
        red_led.write_digital(1)
        music.play("c4:2", pin=buzzer)
        #tps://tech.microbit.org/hardware/edgeconnector/ht 

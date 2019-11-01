from microbit import *
import music
# pins 
crash_sensor = pin11
buzzer = pin0
ad_keypad = pin1
potentiometer = pin3
red_led = pin15
# setup
crash_sensor.set_pull(crash_sensor.PULL_UP)

while True:

    if ad_keypad.read_analog() > 0 and ad_keypad.read_analog() < 10 and potentiometer.read_analog() > 0 and potentiometer.read_analog() <= 511:
        #display.show(all_line_1_beam, delay = 125)
        red_led.write_digital(1)
        music.play("c4:2", pin=buzzer)
    if ad_keypad.read_analog() > 45 and ad_keypad.read_analog() < 55 and potentiometer.read_analog() > 0 and potentiometer.read_analog() <= 511:
        #display.show(all_line_2_beam, delay = 125)
        red_led.write_digital(1)
        music.play("d4:2", pin=buzzer)
    if ad_keypad.read_analog() > 90 and ad_keypad.read_analog() < 100 and potentiometer.read_analog() > 0 and potentiometer.read_analog() <= 511: 
        #display.show(all_line_3_beam, delay = 125)
        red_led.write_digital(1)
        music.play("e4:2", pin=buzzer)
    if ad_keypad.read_analog() > 135 and ad_keypad.read_analog() < 140 and potentiometer.read_analog() > 0 and potentiometer.read_analog() <= 511: 
        #display.show(all_line_4_beam, delay = 125)
        red_led.write_digital(1)
        music.play("f4:2", pin=buzzer)
    if ad_keypad.read_analog() > 535 and ad_keypad.read_analog() < 545 and potentiometer.read_analog() > 0 and potentiometer.read_analog() <= 511:
        #display.show(all_line_5_beam, delay = 125)
        red_led.write_digital(1)
        music.play("g4:2", pin=buzzer)
    if crash_sensor.read_digital() == 0:
        #display.show(all_ripple, delay = 334)
        red_led.write_digital(1)
        music.play(music.FUNK, pin=buzzer)
    elif ad_keypad.read_analog() > 0 and ad_keypad.read_analog() < 10 and potentiometer.read_analog() > 511 and potentiometer.read_analog() <= 1023:
        #display.show(all_line_1_beam, delay = 63)
        red_led.write_digital(1)
        music.play("c8:1", pin=buzzer)
    elif ad_keypad.read_analog() > 45 and ad_keypad.read_analog() < 55 and potentiometer.read_analog() > 511 and potentiometer.read_analog() <= 1023:
        #display.show(all_line_2_beam, delay = 63)
        red_led.write_digital(1)
        music.play("d8:1", pin=buzzer)
    elif ad_keypad.read_analog() > 90 and ad_keypad.read_analog() < 100 and potentiometer.read_analog() > 511 and potentiometer.read_analog() <= 1023: 
        #display.show(all_line_3_beam, delay = 63)
        red_led.write_digital(1)
        music.play("e8:1", pin=buzzer)
    elif ad_keypad.read_analog() > 135 and ad_keypad.read_analog() < 140 and potentiometer.read_analog() > 511 and potentiometer.read_analog() <= 1023: 
        #display.show(all_line_4_beam, delay = 63)
        red_led.write_digital(1)
        music.play("f8:1", pin=buzzer)
    elif ad_keypad.read_analog() > 535 and ad_keypad.read_analog() < 545 and potentiometer.read_analog() > 511 and potentiometer.read_analog() <= 1023:
        # display.show(all_line_5_beam, delay = 63)
        red_led.write_digital(1)
        music.play("g8:1", pin=buzzer)
    else:
        red_led.write_digital(0)
        music.play(music.BLUES)
        # display.show(all_wave, delay = 200, loop = True)
# Write your code here :-)
from microbit import *
import music 

# pins
ADKeypad_pin = pin15
Buzzer_pin = pin16

while True:
    # buttonA 
    if ADKeypad_pin.read_analog() > 0 and ADKeypad_pin.read_analog() < 10:
        music.play('g4:1', pin=Buzzer_pin)
    # buttonB 
    if ADKeypad_pin.read_analog() > 45 and ADKeypad_pin.read_analog() < 55:
        music.play('e4:1', pin=Buzzer_pin)

 
    # buttonC 
    if ADKeypad_pin.read_analog() > 90 and ADKeypad_pin.read_analog() < 100:
        music.play('a4:1', pin=Buzzer_pin)
     
    # buttonD 
    if ADKeypad_pin.read_analog() > 136 and ADKeypad_pin.read_analog() < 139:
        music.play('d4:1', pin=Buzzer_pin)
     
    # buttonE 
    if ADKeypad_pin.read_analog() > 535 and ADKeypad_pin.read_analog() < 545:
      
        music.play('d4:1', pin=Buzzer_pin)


    


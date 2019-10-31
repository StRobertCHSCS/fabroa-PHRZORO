from microbit import *
 
# pins
ADKeypad_pin = pin2
 
while True:
    # buttonA
    if ADKeypad_pin.read_analog() &gt; 0 and ADKeypad_pin.read_analog() &lt; 10:
        display.show(Image.SILLY)                             
 
    # buttonB
    if ADKeypad_pin.read_analog() &gt; 45 and ADKeypad_pin.read_analog() &lt; 55:
        display.show(Image.HAPPY)
 
    # buttonC
    if ADKeypad_pin.read_analog() &gt; 90 and ADKeypad_pin.read_analog() &lt; 100:
        display.show(Image.SKULL)
 
    # buttonD
    if ADKeypad_pin.read_analog() &gt; 135 and ADKeypad_pin.read_analog() &lt; 140:
        display.show(Image.PITCHFORK)
 
    # buttonE
    if ADKeypad_pin.read_analog() &gt; 535 and ADKeypad_pin.read_analog() &lt; 545:
        display.show(Image.DUCK)


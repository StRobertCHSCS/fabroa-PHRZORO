from microbit import *
import random

display.scroll(str(random.randint(1, 100)), loop=True, delay=100)
response = str(input("Hi: "))
if (response == "Hi"):
    print("Nice")
else:
    print("get yeeted")

# code 
from servo import Servo 
import time
servo = Servo(mini_servo)
servo.write_angle(0)
from microbit import *
import music 

# pins 
crash_sensor = pin0
buzzer = pin2
mini_servo = pin3
ad_keypad = pin4
potentiometer = pin6
red_led = pin10
# setup
crash_sensor.set_pull(crash_sensor.PULL_UP)

# animations 
line_1_1_beam = Image("00000:""00000:""00000:""00000:""90000")
line_1_2_beam = Image("00000:""00000:""00000:""90000:""80000")
line_1_3_beam = Image("00000:""00000:""90000:""80000:""70000")
line_1_4_beam = Image("00000:""90000:""80000:""70000:""00000")
line_1_5_beam = Image("90000:""80000:""70000:""00000:""00000")
line_1_6_beam = Image("80000:""70000:""00000:""00000:""00000")
line_1_7_beam = Image("70000:""00000:""00000:""00000:""00000")
line_1_8_beam = Image("00000:""00000:""00000:""00000:""00000")

all_line_1_beam = [line_1_1_beam, line_1_2_beam, line_1_3_beam, line_1_4_beam, line_1_5_beam, line_1_6_beam, line_1_7_beam, line_1_8_beam]

line_2_1_beam = Image("00000:""00000:""00000:""00000:""09000")
line_2_2_beam = Image("00000:""00000:""00000:""09000:""08000")
line_2_3_beam = Image("00000:""00000:""09000:""08000:""07000")
line_2_4_beam = Image("00000:""09000:""08000:""07000:""00000")
line_2_5_beam = Image("09000:""08000:""07000:""00000:""00000")
line_2_6_beam = Image("08000:""07000:""00000:""00000:""00000")
line_2_7_beam = Image("07000:""00000:""00000:""00000:""00000")
line_2_8_beam = Image("00000:""00000:""00000:""00000:""00000")

all_line_2_beam = [line_2_1_beam, line_2_2_beam, line_2_3_beam, line_2_4_beam, line_2_5_beam, line_2_6_beam, line_2_7_beam, line_2_8_beam]

line_3_1_beam = Image("00000:""00000:""00000:""00000:""00900")
line_3_2_beam = Image("00000:""00000:""00000:""00900:""00800")
line_3_3_beam = Image("00000:""00000:""00900:""00800:""00700")
line_3_4_beam = Image("00000:""00900:""00800:""00700:""00000")
line_3_5_beam = Image("00900:""00800:""00700:""00000:""00000")
line_3_6_beam = Image("00800:""00700:""00000:""00000:""00000")
line_3_7_beam = Image("00700:""00000:""00000:""00000:""00000")
line_3_8_beam = Image("00000:""00000:""00000:""00000:""00000")

all_line_3_beam = [line_3_1_beam, line_3_2_beam, line_3_3_beam, line_3_4_beam, line_3_5_beam, line_3_6_beam, line_3_7_beam, line_3_8_beam]

line_4_1_beam = Image("00000:""00000:""00000:""00000:""00090")
line_4_2_beam = Image("00000:""00000:""00000:""00090:""00080")
line_4_3_beam = Image("00000:""00000:""00090:""00080:""00070")
line_4_4_beam = Image("00000:""00090:""00080:""00070:""00000")
line_4_5_beam = Image("00090:""00080:""00070:""00000:""00000")
line_4_6_beam = Image("00080:""00070:""00000:""00000:""00000")
line_4_7_beam = Image("00070:""00000:""00000:""00000:""00000")
line_4_8_beam = Image("00000:""00000:""00000:""00000:""00000")

all_line_4_beam = [line_4_1_beam, line_4_2_beam, line_4_3_beam, line_4_4_beam, line_4_5_beam, line_4_6_beam, line_4_7_beam, line_4_8_beam]

line_5_1_beam = Image("00000:""00000:""00000:""00000:""00009")
line_5_2_beam = Image("00000:""00000:""00000:""00009:""00008")
line_5_3_beam = Image("00000:""00000:""00009:""00008:""00007")
line_5_4_beam = Image("00000:""00009:""00008:""00007:""00000")
line_5_5_beam = Image("00009:""00008:""00007:""00000:""00000")
line_5_6_beam = Image("00008:""00007:""00000:""00000:""00000")
line_5_7_beam = Image("00007:""00000:""00000:""00000:""00000")
line_5_8_beam = Image("00000:""00000:""00000:""00000:""00000")

all_line_5_beam = [line_5_1_beam, line_5_2_beam, line_5_3_beam, line_5_4_beam, line_5_5_beam, line_5_6_beam, line_5_7_beam, line_5_8_beam]

wave_1 = Image("00000:""00000:""00000:""00000:""99999")
wave_2 = Image("00000:""00000:""00000:""00900:""99899")
wave_3 = Image("00000:""00000:""00900:""09890:""98789")
wave_4 = Image("00000:""00900:""09890:""98789:""87678")
wave_5 = Image("00900:""09890:""98789:""87678:""76567")

all_wave = [wave_1, wave_2, wave_3, wave_4, wave_5]

ripple_1 = Image("00000:""00000:""00900:""00000:""00000")
ripple_2 = Image("00000:""09990:""09090:""09990:""00000")
ripple_3 = Image("99999:""90009:""90009:""90009:""99999")

all_ripple = [ripple_1, ripple_2, ripple_3]
while True: 
    if ad_keypad.read_analog() > 0 and ad_keypad.read_analog() < 10 and potentiometer.read_analog() > 0 and potentiometer.read_analog < 511:
        display.show(all_line_1_beam, )
        servo.write_angle(45)
        time.sleep(1)
        red_led.write_digital(1)
        music.play("c4:4")




from microbit import *
import music 
# pins 
crash_sensor = pin0
buzzer = pin1
pir_sensor = pin2
ad_keypad = pin3
potentiometer = pin4
red_led = pin5
blue_led = pin6
green_led = pin7
# setup
crash_sensor.set_pull(crash_sensor.PULL_UP)
# code 
line_1_1_beam = Image("00000""00000""00000""00000""90000")
line_1_2_beam = Image("00000""00000""00000""90000""80000")
line_1_3_beam = Image("00000""00000""90000""80000""70000")
line_1_4_beam = Image("00000""90000""80000""70000""00000")
line_1_5_beam = Image("90000""80000""70000""00000""00000")
line_1_6_beam = Image("80000""70000""00000""00000""00000")
line_1_7_beam = Image("70000""00000""00000""00000""00000")
line_1_8_beam = Image("00000""00000""00000""00000""00000")

line_1_beam = [line_1_1_beam, line_1_2_beam, line_1_3_beam, line_1_4_beam, line_1_5_beam, line_1_6_beam, line_1_7_beam, line_1_8_beam]

line_2_1_beam = Image("00000""00000""00000""00000""09000")
line_2_2_beam = Image("00000""00000""00000""09000""08000")
line_2_3_beam = Image("00000""00000""09000""08000""07000")
line_2_4_beam = Image("00000""09000""08000""07000""00000")
line_2_5_beam = Image("09000""08000""07000""00000""00000")
line_2_6_beam = Image("08000""07000""00000""00000""00000")
line_2_7_beam = Image("07000""00000""00000""00000""00000")
line_2_8_beam = Image("00000""00000""00000""00000""00000")

line_2_beam = [line_2_1_beam, line_2_2_beam, line_2_3_beam, line_2_4_beam, line_2_5_beam, line_2_6_beam, line_2_7_beam, line_2_8_beam]

line_3_1_beam = Image("00000""00000""00000""00000""00900")
line_3_2_beam = Image("00000""00000""00000""00900""00800")
line_3_3_beam = Image("00000""00000""00900""00800""00700")
line_3_4_beam = Image("00000""00900""00800""00700""00000")
line_3_5_beam = Image("00900""00800""00700""00000""00000")
line_3_6_beam = Image("00800""00700""00000""00000""00000")
line_3_7_beam = Image("00700""00000""00000""00000""00000")
line_3_8_beam = Image("00000""00000""00000""00000""00000")

line_3_beam = [line_3_1_beam, line_3_2_beam, line_3_3_beam, line_3_4_beam, line_3_5_beam, line_3_6_beam, line_3_7_beam, line_3_8_beam]

line_4_1_beam = Image("00000""00000""00000""00000""00090")
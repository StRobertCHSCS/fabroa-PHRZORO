'''
-------------------------------------------------------------------------------
Name: livehack2_problem1.py
Purpose: Takes weight (in kilograms) and height (in meters) and calculates your
bmi. Then, displays whether you are overweight, underwweight or normal
according to your bmi.

Author: Ma.C

Created: 18/11/2019
------------------------------------------------------------------------------
'''

# get weight in kilograms
weight = float(input("Enter your weight (kg): "))

# get height in meters
height = float(input("Enter your height (m) : "))

# calculate bmi by multiplying the height by itself, then dividing the product
# by the weight
bmi = weight / (height*height)

# if bmi is greater than 25, then print "You are overweight."
if bmi > 25:
    print("You are overweight.")

# if bmi is less than 18.5, then print "You are underweight."
elif bmi < 18.5:
    print("You are underweight.")

# if the above two conditions are not met and your bmi is between 18.5 and 25,
# then print "Your weight is normal."
else:
    print("Your weight is normal.")

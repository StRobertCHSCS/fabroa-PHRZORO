'''
-------------------------------------------------------------------------------
Name: problem.py
Purpose: Convert degrees in fahrenheit to celsius

Author:	Ma.C

Created: 02/10/2019
------------------------------------------------------------------------------
'''

# print purpose of program
print("****** Welcome to the Celsius to Fahrenheit Converter ******")

# get degree in celsius from user
celsius = float(input("Enter the degrees in Celsius: "))

# compute degree in fahrenheit by multiplying degree in celsius by 9/5,
# then adding 32
fahrenheit = (9/5)*celsius + 32

# print degrees in fahrenheit
print("This is", fahrenheit, "degrees fahrenheit.")

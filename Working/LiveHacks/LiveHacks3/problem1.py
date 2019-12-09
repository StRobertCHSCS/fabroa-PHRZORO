'''
-------------------------------------------------------------------------------
Name: problem1.py
Purpose: Allows user to input number of days to track, then allows user to 
input temperature for each day. Outputs the number of heating days 
(temperature below 15). 

Author: Ma.C

Created: 09/12/2019 
------------------------------------------------------------------------------
'''
# display starting message 
print("****** Heating Days Tracker ******")

# init heating variable 
heating = 0 

# obtain number of days to track 
days = int(input("Enter the number of days to track: "))

# for inputed number of days repeat this code 
for temperature in range(days):

    # get temperature 
    temperature = int(input(""))

    # if temperature is less than 15 then add 1 to heating 
    if temperature < 15: 

        heating = heating + 1

# output number of haeting days 
print("There are", heating, "heating days.")
    
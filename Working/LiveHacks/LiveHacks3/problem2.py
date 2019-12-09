'''
-------------------------------------------------------------------------------
Name: problem2.py
Purpose: Allows user to input distance driven per day until total distance is 
greater than 100 km. Then outputs number of days taken to surpass 100 km. 
Calculates and outputs average distance driven per day. 

Author: Ma.C

Created: 09/12/2019 
------------------------------------------------------------------------------
'''
# display starting message 
print("**** Welcome to the Distance Tracker ****")

# init days variable 
days = 0 

# init total_dist variable 
total_dist = 0

# while total distance is less than 100 repeat this code 
while total_dist < 100: 

    # get distance 
    distance = int(input("Enter the distance travelled for the day: "))

    # calculate total distance by adding inputed distance 
    total_dist += distance

    # increment number of days 
    days += 1 

# print number of days taken to surpass 100 km
print("It took", days, "days to surpass 100 km driven.")

# calculate and print average distance 
print("The average distance driven per day is", total_dist/days, "km.")

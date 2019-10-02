'''
-------------------------------------------------------------------------------
Name: problem2.py
Purpose: Divide pieces of chicken evenly between students and display leftovers

Author:	Ma.C

Created: 02/10/2019
------------------------------------------------------------------------------
'''

# print purpose of program
print("****** Welcome to the fried chicken distributor ******")

# get amount of chicken and number of students
chicken = int(input("Enter pieces of fried chicken: "))
students = int(input("Enter number of students: "))

# compute chicken recieved by dividing chicken by students,
# and finding remainder
chicken_recieved = chicken // students
leftover = chicken % students

# print amount of chicken recived per student and chicken leftover
print("Each student will recieve", chicken_recieved, "piece(s) of chicken,")
print("there will be", leftover, "piece(s) leftover.")

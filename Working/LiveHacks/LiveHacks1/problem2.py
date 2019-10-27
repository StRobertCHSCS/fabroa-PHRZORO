'''
-------------------------------------------------------------------------------
Name: problem2.py
Purpose: Divide pieces of chicken evenly between students and display leftovers

Author:	Ma.C

Created: 02/10/2019
------------------------------------------------------------------------------
'''

print("****** Welcome to the fried chicken distributor ******")

chicken = int(input("Enter pieces of fried chicken: "))
students = int(input("Enter number of students: "))


if (chicken == 0) and (students >0): 
    print(students, "students starve to death")
if (students == 0) and (chicken == 0):
    print("Please kindly exit")
elif(students > chicken) and (chicken > 0):
    print("There isn't enough to share!")
    print("The teacher gets", chicken, "pieces of chicken")
elif students <= chicken and (chicken > 0): 
    chicken_recieved = chicken // students
    leftover = chicken % students
    print("Students will get", chicken_recieved, "pieces of chicken")
    print("The teacher will get", leftover, "pieces of chicken")







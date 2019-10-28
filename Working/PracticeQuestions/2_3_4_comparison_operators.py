age = 33

# Note that each branch below only gets
# reached IF every prior branch had
# a condition that evaluated to False.
if age < 18:
    print("0 - 17")
elif age < 26:
    print("18 - 25")
elif age < 36:
    print("26 - 35")
elif age < 46:
    print("36 - 45")
elif age < 56:
    print("46 - 55")
elif age < 66:
    print("56 - 65")
else:
    print("66+")
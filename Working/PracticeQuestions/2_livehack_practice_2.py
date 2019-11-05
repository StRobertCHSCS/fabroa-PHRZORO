earnings = int(input("How much did you earn? "))
mark_1 = int(input("Input your first mark: "))
mark_2 = int(input("Input your second mark: "))
mark_3 = int(input("Input your third mark: "))
mark_4 = int(input("Input your fourth mark: "))
mark_5 = int(input("Input your fifth mark: "))
mark_6 = int(input("Input your last mark: "))
if (earnings >= 500 and
        ((mark_1 + mark_2 + mark_3 + mark_4 + mark_5 + mark_6) / 6) > 80):
    print("You can go to Europe fro the sumnmer. ")
elif (earnings < 500 and
        ((mark_1 + mark_2 + mark_3 + mark_4 + mark_5 + mark_6) / 6) > 80):
    print("you can go to California for the summer. ")
else:
    print("you failed. ")
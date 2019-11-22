total = 0 
num_num = int(input("Enter the number of numbers: "))
for i in range(num_num):
    number = int(input("Enter your number(s): "))
    total = total + number 
print(num_num)
print("Sum: "total)
start = int(input("Enter the first number: "))
end = int(input("Enter the last number: "))
if start < end: 
    for i in range(start, end + 1, 1):
        print(i)
else: 
    for i in range(start, end - 1, -1):
        print(i)

n = int(input("Enter your number: "))
while n < 2:
    n = int(input("Enter your number (not less than 2): "))
i = 2
while i < n:
    if n // i * i == n: 
        print(i)
        break
    else: 
        i += 1
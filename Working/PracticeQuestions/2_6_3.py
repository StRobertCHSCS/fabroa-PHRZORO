n = int(input("Enter your number: "))
i = n
while i <=n:
    if 2 ** i < n: 
        print("exponent:", i)
        print("2**n:", 2**i)
        break
    else: 
        i -= 1


total = 0 
for i in range(3):
    price = float(input("Enter the price of the product: "))
    quantity = int(input("Enter the quantity of the product: "))
    total = total + price * quantity
com_total = (total * 1.13)
print(com_total)
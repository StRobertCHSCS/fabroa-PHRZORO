#print the header with string formatting
print("{0:>10}{1:>10}".format("Ounces","Grams"))
print("-"*20)  #table header line

#build and output the rows
for i in range(1,16):
    print("{0:10}{1:10.2f}".format(i, i * 28.35)

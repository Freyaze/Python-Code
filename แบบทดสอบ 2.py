amount = 0

for n in range(1, 8):
    amount = float(input("Enter amount of day " + str(n) + " : "))
    while amount >= 1000000:
        print()

vat = amount * 7 / 107
sales = amount - vat 
print()      





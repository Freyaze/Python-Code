from random import uniform

total = 0.0
strInput = ""
for n in range(1, 6):
    num = round(uniform(30.0, 50.0), 2)
    total += num 
    strInput += str(num) + ","
    
average = round(total/5)
print("Value random : ", strInput)
print("Total = ", round(total, 2))
print("Average =", average)

score = 0 
grade = ""
result = "      Report Grade\n+=====================+\n"
result += "| No. | Score | Grade |\n+=====================+\n"
total = 0 
Max = Min = 0
for n in range(1,6):
    score = int(input("Enter score#"+str(n)+" : "))
    if score >= 80: grade = "A"
    elif score >= 70: grade = "B"
    elif score >= 60: grade = "C"
    elif score >= 50: grade = "D"
    else: grade = "F"
    result += "|  " + str(n) + "  |  " + format(score,">3") + "  |   " + grade + "  |\n"
    total += score
    if n == 1: Max = Min = score
    else:
        Max = max(Max, score)
        Min = min(Min, score)
result += "\n+=====================+\n"
result += "|Average Score| " + format(total/5,".2f") + " |\n"
result += "|Maximum Score| " + format(Max, ">5") + " |\n"
result += "|Minimum Score| " + format(Min, ">5") + " |\n"
print(result)
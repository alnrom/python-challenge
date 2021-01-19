import os
import csv
import numpy as np

csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')

monthslist = []
total = [] # Profit/Loses column
changes = []


with open(csvpath) as file:
    lines = csv.reader(file, delimiter=",")
    next(lines, None) #skips header
    for line in lines:
        monthslist.append(line) #creates list
        total_months = len(monthslist) 

        total.append(int(line[1])) #creates list with only the profit/lose
        Net_total = sum(total)

        list1 = np.array(total[1:]) #totals from 2nd month on
        list2 = np.array(total[:-1]) #total until last month -1
        changes = list1 - list2
    Average_change = round(sum(changes)/len(changes),2)
    greatest_increased = max(changes)
    greatest_decreased = min(changes)
    
    #greatest_increased_month = monthslist.index(greatest_increased)
    #greatest_decreased_month = monthslist.index(greatest_decreased)

print("--------------")
print("Financial Analysis")
print(f"Total Months: {total_months}")
print(f"Total: {Net_total}")
print(f"Average change: {Average_change}")
print(f"Greatest increased in profits: ${greatest_increased}")
print(f"Greatest decreased in profits: ${greatest_decreased}")


f = open("PyBank.txt", "w")
print("--------------", file=  f)
print("Financial Analysis", file = f)
print(f"Total Months: {total_months}", file=  f)
print(f"Total: {Net_total}", file=  f)
print(f"Average change: {Average_change}", file=  f)
print(f"Greatest increased in profits: ${greatest_increased}", file=  f)
print(f"Greatest decreased in profits: ${greatest_decreased}", file=  f)
f.close()






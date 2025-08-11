# create a list expenses [10000,12000,13000,14000]
# update 12000 as 12500
# display all expenses
# display highest expense
# display avg expense

expense = [10000, 12000, 13000, 14000]
expense[1] = 12500
print(f"all expense : {expense}")
sum = 0
for total in expense:
    sum +=  total
print(f"total expense is {sum}")
h_expense = max(expense)
print(f"highest expense is :{h_expense}")
avg_expense = sum /len(expense)
print(f"average is {avg_expense}")
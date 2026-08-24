budget = int(input("What is your total budget? "))

items = int(input("How many expenses do you want to add? "))
item = []
expense =[]
total = 0


for i in range(items):
    item.append(input(f"Expense {i+1} for what: "))
    expense.append(int(input(f"Amount {i+1}: ")))
    total = total+expense[i]


# Print Statement
for i in range (items):
    print(item[i], "=", expense[i])

print("_________________________")
print("Total Expense =", total)
rem_budget = budget-total
print("Remaining Budget =", rem_budget)
print("_________________________")
if(rem_budget>0):
    print("You are within your budget!")
else:
    print("You Exceeded your limit.... ")
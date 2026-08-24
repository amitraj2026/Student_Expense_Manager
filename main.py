'''
STUDENT EXPENSE AND BUDGET MANAGER
===Feature===
1. Add Expense
2. View All Expense
3. Total Expense
4. Category wise expense
5. Heighest Expense
6. Exit
'''

num = int(input("How much expense do you want to add: "))
expenses = []
count = 0

for i in range(num):

    expenses.append(input(f"Name of Expense {i+1}: "))
    expenses.append(int(input(f"Total Price of {expenses[count]}: ")))
    count += 2


print(expenses)
    
'''
STUDENT EXPENSE AND BUDGET MANAGER
===Feature===
1. Set Budget
2. Add Expense
3. View All Expenses
4. Category wise expense
5. Unique Categories
6. Highest Expense
7. Budget Status
8. Exit
'''

# Functions
# 1. Set Budget
def set_budget():
    print("===== STUDENT EXPENSE MANAGER =====")
    budget = int(input("Enter your monthly budget: "))
    print("\nBudget set successfully! ✅")
    print("Your budget:", budget) 
    return budget  

#2. Add Expense
def add_expense(expenses):

    num = int(input("How much expense do you want to add: "))

    for i in range(num):
        name = input("Enter expense name: ")
        amount = int(input("Enter amount: "))
        category = input("Enter category: ")
        expense = (name, amount, category)
        expenses.append(expense)
        print("Expense added successfully! ✅ \n")

    return expenses

#3. View All Expenses
def all_expenses(expenses):
    total_expense = 0
    for expense in expenses:
        name, amount, category = expense  #Tuple unpacking
        total_expense += amount
        print(f"{name} | {amount} | {category}")

    print(f"Total Expenses = {total_expense}")
    return total_expense

#4. Category-wise Expense
def category_expenses(expenses):
    category_expenses = {}
    
    for expense in expenses:
        name, amount, category = expense
        if category in category_expenses:
            category_expenses[category] += amount
        else:
            category_expenses[category] = amount
    
    # Print Category
    for category, amount in category_expenses.items():
        print(f"{category} : ₹{amount}")

#5. Unique Categories
def unique_categories(expenses):
    categories = set()

    for expense in expenses:
        name, amount, category = expense
        categories.add(category)

    for category in categories:
        print(category)

#6. Highest Expense
def highest_expense(expenses):
    highest = 0
    highest_cat ="" 
    for expense in expenses:
        name, amount, category = expense
        if(amount>highest):
            highest = amount
            highest_cat = name

    print(f"{highest_cat} : {highest}")


#7. Budget Status
def budget_status(budget, total_expense):
    print("==== Budget Status ====/\n")
    print(f"Monthly Budget: ₹{budget}")
    print(f"Total Expense: ₹{total_expense}")
    print(f"Remaining: ₹{budget-total_expense}")

    if remaining >= 0:
        print(f"Remaining: ₹{remaining}")
        print("Status: ✅ Within Budget")
    else:
        print(f"Budget Exceeded By: ₹{abs(remaining)}")
        print("Status: ⚠️ Budget Exceeded")



budget = 0
expenses = []
total_expense = 0

while True:

    print("\n===== STUDENT EXPENSE MANAGER =====")
    print("1. Add Budget")
    print("2. Add Expense")
    print("3. View All Expenses")
    print("4. Category-wise Expense")
    print("5. Unique Categories")
    print("6. Highest Expense")
    print("7. Budget Status")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            budget = set_budget()

        case 2:
            expenses = add_expense(expenses)
        case 3:
            total_expense = all_expenses(expenses)
        case 4:
            category_expenses(expenses)
        case 5:
            unique_categories(expenses)
        case 6:
            highest_expense(expenses)
        case 7:
            budget_status(budget, total_expense)
        case 8:
            print("Thank you for using Student Expense Manager! 👋")
            break
        case _:
            print("Invalid choice ❌")


#Budget Tracker
income = float(input("Enter your monthly income: "))

food = float(input("Enter food expense: "))
rent = float(input("Enter rent expense: "))
entertainment = float(input("Enter entertainment expense: "))
other = float(input("Enter other expenses: "))
#  Calculating total and remaining Expense
total_expenses = food + rent + entertainment + other
remaining_budget = income - total_expenses
# For Display
print("\n------ Budget Summary ------")
print("Income:", income)
print("Food Expense:", food)
print("Rent Expense:", rent)
print("Entertainment Expense:", entertainment)
print("Other Expenses:", other)
print("-----------------------------")
print("Total Expenses:", total_expenses)
print("Remaining Budget:", remaining_budget)
print("\n------ Budget Summary ------")
print("Income:", income)
print("Food Expense:", food)
print("Rent Expense:", rent)
print("Entertainment Expense:", entertainment)
print("Other Expenses:", other)
print("-----------------------------")
print("Total Expenses:", total_expenses)
print("Remaining Budget:", remaining_budget)

# Condition checking
if remaining_budget < 0:
    print("Warning: You spent more than your income!")
else:
    print("Good! You are within your budget.")
# Saving data in CSV file
file = open("budget_data.csv", "a")

data = f"{income},{food},{rent},{entertainment},{other},{remaining_budget}\n"

file.write(data)

file.close()
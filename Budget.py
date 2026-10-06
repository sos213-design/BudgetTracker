def CalculateBudget(income, TotalExpense):
    return income - TotalExpense



income = int(input("Enter Income: "))
expenses = [] # Will hold all the expenses as a list

expense = int(input("Enter Expense: "))
while expense != 0:
    expenses.append(expense)
    expense = int(input("Enter Expense (type 0 when finished): "))

TotalExpense = sum(expenses)
Budget = CalculateBudget(income, TotalExpense)

Ques = input("Do You want to see your budget? (y/n): ")

if Ques == "y":
    print("Budget:", Budget)

else:
    print("Okay Cool")


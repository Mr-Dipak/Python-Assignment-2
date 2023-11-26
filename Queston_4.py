"""
3. Your monthly expense list (from Jan to May) looks like this,

expense_list = [2340, 2500, 2100, 3100, 2980]

Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred.
If expense is not found then it should print that as well.

"""

n = int(input("Enter expense amount: "))

expense_list = [2340, 2500, 2100, 3100, 2980]

month_index = None

for i, expense in enumerate(expense_list):
    if (expense == n):
        month_index = i
        break

if month_index is not None:
    print(f"The expense {n} is occured in month {month_index+1}.")
else:
    print(f"The expense {n} is not occured in any month")

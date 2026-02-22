import os
from modules.expense import Expense

FILE_PATH = "data/expenses.txt"

def save_expense(expense):
    os.makedirs("data", exist_ok=True)
    with open(FILE_PATH, "a") as f:
        f.write(expense.to_file_string() + "\n")

def load_expenses():
    expenses = []
    if not os.path.exists(FILE_PATH):
        return expenses

    try:
        with open(FILE_PATH, "r") as f:
            for line in f:
                expense = Expense.from_file_string(line)
                if expense:
                    expenses.append(expense)
    except Exception:
        print("Error reading file.")
    return expenses

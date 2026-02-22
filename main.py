from modules.expense import Expense
from modules.file_operations import save_expense, load_expenses
from modules.category_summarizer import summarize_by_category


def add_expense():
    amount_input = input("Enter amount: ").strip()
    amount = Expense.validate_amount(amount_input)

    if amount is None:
        print("Invalid amount. Please enter a positive number.")
        return

    category = input("Enter category: ").strip()
    if not category:
        print("Category cannot be empty.")
        return

    date = input("Enter date (YYYY-MM-DD): ").strip()
    if not Expense.validate_date(date):
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    expense = Expense(amount, category, date)
    save_expense(expense)
    print("Expense added successfully!")


def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- All Expenses ---")
    print(f"{'Amount':<10}{'Category':<15}{'Date':<12}")
    print("-" * 37)

    for exp in expenses:
        print(f"{exp.amount:<10.2f}{exp.category:<15}{exp.date:<12}")


def summarize_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses to summarize.")
        return

    summary = summarize_by_category(expenses)

    print("\n--- Expense Summary by Category ---")
    print(f"{'Category':<15}{'Total Amount'}")
    print("-" * 30)

    for category, total in summary.items():
        print(f"{category:<15}{total:.2f}")


def main():
    while True:
        print("\n====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summarize by Category")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summarize_expenses()
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

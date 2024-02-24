import datetime

# Define the Expense class
class Expense:
    def __init__(self, amount, category, description, date=None):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date or datetime.date.today()

    def __str__(self):
        return f"{self.date} - {self.amount} - {self.category} - {self.description}"

# Functions for the expense tracker
def add_expense(expenses):
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    description = input("Enter expense description: ")
    expense = Expense(amount, category, description)
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully.\n")

def list_expenses(expenses):
    for expense in expenses:
        print(expense)
    if not expenses:
        print("No expenses recorded.\n")

def calculate_total_expenses(expenses):
    return sum(expense.amount for expense in expenses)

def monthly_report(expenses):
    monthly_expenses = {}
    for expense in expenses:
        if expense.date.strftime('%Y-%m') not in monthly_expenses:
            monthly_expenses[expense.date.strftime('%Y-%m')] = expense.amount
        else:
            monthly_expenses[expense.date.strftime('%Y-%m')] += expense.amount
    for month, total in monthly_expenses.items():
        print(f"{month}: {total}")

def save_expenses(expenses):
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(f"{expense.date},{expense.amount},{expense.category},{expense.description}\n")

def load_expenses():
    expenses = []
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                date_str, amount, category, description = line.strip().split(',')
                date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
                expenses.append(Expense(float(amount), category, description, date))
    except FileNotFoundError:
        pass
    return expenses

def main():
    expenses = load_expenses()

    while True:
        print("1. Add expense")
        print("2. List expenses")
        print("3. Calculate total expenses")
        print("4. Generate monthly report")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            total = calculate_total_expenses(expenses)
            print(f"Total Expenses: {total}\n")
        elif choice == "4":
            monthly_report(expenses)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")

if __name__ == "__main__":
    main()

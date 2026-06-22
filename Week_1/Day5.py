# Read and write text file  
# Open a file for writing
file = open("trial.txt", "w")
file.write("Hello, this is a test.")
file.close()

# Open the file for reading
file = open("trial.txt", "r")
content = file.read()
print(content)
file.close()


# Simple Expense Tracker using Exception Handling, Decorators, File Handling

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        try:
            with open("expenses.txt", "r") as file:
                for line in file:
                    amount, category = line.strip().split(",")
                    self.expenses.append((float(amount), category))
        except FileNotFoundError:
            print("No previous expenses found. Starting fresh.")

    def save_expenses(self):
        with open("expenses.txt", "w") as file:
            for amount, category in self.expenses:
                file.write(f"{amount},{category}\n")

    def add_expense(self, amount, category):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        self.expenses.append((amount, category))
        self.save_expenses()

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        for amount, category in self.expenses:
            print(f"Amount: {amount}, Category: {category}")
            print("-" * 30)

s1 = ExpenseTracker()
while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            s1.add_expense(amount, category)
            print("Expense added successfully.")
        except ValueError as e:
            print(f"Error: {e}")
    elif choice == "2":
        s1.view_expenses()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")
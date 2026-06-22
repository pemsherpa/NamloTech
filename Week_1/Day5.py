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


# Simple Expense Tracker

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category):
        self.expenses.append({"amount": amount, "category": category})

    def total_expenses(self):
        return sum(expense["amount"] for expense in self.expenses)

    def expenses_by_category(self, category):
        return sum(expense["amount"] for expense in self.expenses if expense["category"] == category)
    
tracker = ExpenseTracker()
tracker.add_expense(50, "Food")
tracker.add_expense(20, "Transport")
tracker.add_expense(30, "Food")

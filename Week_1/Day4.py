# Student Class

class Student:
    def __init__(self):
        self.name = input("Enter student name: ")
        self.age = int(input("Enter age: "))
        self.grade = input("Enter grade: ")

    def display_info(self):
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)

s1 = Student()
s1.display_info()


# bank account class

class BankAccount:
    def __init__(self):
        self.account_number = input("Enter account number: ")
        self.account_holder = input("Enter name of account holder: ")
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited:", amount)
        else:
            print("Invalid deposit amount")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("not enough money with you")
        elif amount <=0:
            print("Invalid withdraw amount")
        else:
            self.balance -= amount
            print("Amount withdrawn:", amount)
    
    def display_balance(self):
        print("Current balance:", self.balance)

a1 = BankAccount()
a1.deposit(1000)
a1.withdraw(500)
a1.display_balance()

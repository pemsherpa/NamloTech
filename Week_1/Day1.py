def EvenOrOdd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
    
print(EvenOrOdd(4))

# Calculator

import math
def Addition(a,b):
    return a+b

def Subtraction(a,b):
    return a-b

def Multiplication(a,b):    
    return a*b

def Division(a,b):
    if b == 0:
        return "Error: Division by zero"
    else:
        return a/b
    
def SquareRoot(a):
    if a < 0:
        return "Error: Square root of negative number"
    else:
        return math.sqrt(a)

def Power(a,b):
    return a**b
    
def Calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Power")

    choice = int(input("Enter choice(1,2,3,4,5,6): "))

    if choice in [1,2,3,4,6]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    else:
        num1 = float(input("Enter number: "))

    if choice == 1:
        print(num1, "+", num2, "=", Addition(num1,num2))
    elif choice == 2:
        print(num1, "-", num2, "=", Subtraction(num1,num2))
    elif choice == 3:           
        print(num1, "*", num2, "=", Multiplication(num1,num2))
    elif choice == 4:
        print(num1, "/", num2, "=", Division(num1,num2))
    elif choice == 5:
        print("Square root of", num1, "=", SquareRoot(num1))
    elif choice == 6:
        print(num1, "^", num2, "=", Power(num1,num2))
    else:
        print("Invalid input")

Calculator()

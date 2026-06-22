#factorial

def factorial(n):
    if n<0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = factorial(n-1) * n
        return result
    
print(factorial(5))

# Prime Number check

def PrimeOrNot(n):
    if n<=1:
        return "Not a prime number"
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return "Not a prime number"
    return "Prime number"

print(PrimeOrNot(10))

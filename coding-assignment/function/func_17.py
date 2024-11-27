# Find the Factorial of a Number

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
print(factorial(3))  # 6

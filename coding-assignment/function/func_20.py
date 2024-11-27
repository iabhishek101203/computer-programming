# Generate Fibonacci Sequence Up to n Terms
# python
# Copy code

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(fibonacci(5))  # [0, 1, 1, 2, 3]
print(fibonacci(8))  # [0, 1, 1, 2, 3, 5, 8, 13]

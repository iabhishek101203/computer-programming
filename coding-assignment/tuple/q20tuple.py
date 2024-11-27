# Write a Python program to replace last value of tuples in a list

# Sample Output

# [(5, 2, 3), (4, 7, 6), (8, 9, 6)]

# Replace value = 10

# [(5, 2, 10),(4, 7, 10),(8, 9, 10)]

l = [(5, 2, 3), (4, 7, 6), (8, 9, 6)]
print([t[:-1] + (10,) for t in l])
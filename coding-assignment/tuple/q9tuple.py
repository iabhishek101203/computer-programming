# Write a Python program to remove an item from a tuple

# Sample Output

# (23, 45, 56, 68, 10, 45, 7, 9)

# Remove = 56

# (23, 45, 68, 10, 45, 7, 9)
a = (23,45,56,68,10,45,7,9)
print("Original A :",a)
b = list(a)
b.remove(56)
a = tuple(b)
print("After Removing A :",a)
print(type(a))
 
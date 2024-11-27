#  Write a Python program to compute element-wise sum of given tuples

# Sample Output

# A = (2, 5, 8)

# B = (6, 5, 1)

# C = (1, 4, 7)

# D = (3, 7, 2)

# Sum of Elements = (12, 21, 18)

a = (2, 5, 8)
b = (6, 5, 1)
c = (1, 4, 7)
d = (3, 7, 2)
print("A :",a)
print("B :",b)
print("C :",c)
print("D :",d)
res = tuple(map(sum, zip(a, b, c, d)))
print("Sum of Elements:",res)
 
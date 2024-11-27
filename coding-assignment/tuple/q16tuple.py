#  Swap two tuples in Python

# Sample Output

# Before Swap A : 10

# Before Swap B : 20

# After Swap A : 20

# After Swap B : 10
a=10
b=20
print("Before Swap A :",a)
print("Before Swap b :",b)
#First Method
#a , b = b, a
t = a
a = b
b = a
print("After Swap A :",a)
print("After Swap b :",b)
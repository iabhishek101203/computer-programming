# Write a Python program to change a given string to a new string where the first and last chars have been exchanged

# Sample Output

# Before Exchange = Python

# After Exchange = nythoP

str = "Python"
print("Before Swap :",str)
s = str[0]
e = str[-1]
res = e + str[1:-1] + s
print("After Swap :",res)
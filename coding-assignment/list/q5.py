# Write a Python program to get the largest number from a list

# Sample Output

# [1,7,10,34,2,8]

# Largest Number : 34

a=[1,7,10,34,2,8]
"""
print("Largest Number :",max(a))
"""
max = a[ 0 ]
for i in a:
	if i > max:
		max = i
print("Largest Number :",max)
 
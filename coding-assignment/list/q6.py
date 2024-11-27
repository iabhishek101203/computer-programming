# . Write a Python program to get the smallest number from a list

# Sample Output

# [51,7,10,34,2,8]

# Smallest Number : 2

a=[51,7,10,34,2,8]
"""
print("Smallest Number :",min(a))
"""
min_num = a[0]
for i in a:
	if i < min_num:
		min_num = i
print("Smallest Number :",min_num)
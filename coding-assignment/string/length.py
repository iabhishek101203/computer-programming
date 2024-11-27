#  Write a Python function to reverses a string if it's length is a multiple of 4.

# Sample Output

# Enter the String = Computer

# If the length is a multiple of 4 = retupmoC

# Enter the String = Science

# If the length is not a multiple of 4 = Science

str=input("Enter the String :")
if len(str) % 4 == 0:
   print(''.join(reversed(str)))
else:
	print(str)
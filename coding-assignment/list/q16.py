# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30

# Sample Output

# First 5 elements : [1, 4, 9, 16, 25]

# Last 5 elements : [625, 676, 729, 784, 841]
l = list()
for i in range(11,25):
	l.append(i**2)
print(l[:5])
print(l[-5:])
# Write a Python program to print the numbers of a specified list after removing even numbers from it

# Sample Output

# [7,32,81,20,25,14,23,27]

# [7, 81, 25, 23, 27]

n = [7,32,81,20,25,14,23,27]
n = [x for x in n if x%2!=0]
print(n)
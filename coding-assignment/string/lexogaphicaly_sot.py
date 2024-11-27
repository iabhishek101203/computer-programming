#  Write a Python program to sort a string lexicographically.

# Sample Output

# Enter the String = Tutor

# ['o', 'r', 'T', 't', 'u']
s=input("Enter the String :")
print(sorted(sorted(s), key=str.upper))
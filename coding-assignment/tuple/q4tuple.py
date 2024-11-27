#  Write a Python program to get the 4th element and 4th element from last of a tuple

# Sample Output

# ('w', 3, 'r', 'e', 's', 'o', 'u', 'r', 'c', 'e')

# 4th Elements From Tuple : e

# 4th Elements From Last Tuple : u
t = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
print(t)
#Get item (4th element)of the tuple by index
i = t[3]
print("4th Elements From Tuple :",i)
#Get item (4th element from last)by index negative
j = t[-4]
print("4th Elements From Last Tuple :",j)
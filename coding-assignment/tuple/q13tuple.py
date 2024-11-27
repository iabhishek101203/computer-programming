# Write a Python program to unzip a list of tuples into individual lists

# Sample Output

# [ (10,30), (60,90), (20,50) ]

# [ (10, 60, 20), (30, 90, 50) ]
# aaaaaannsssssss


l = [(10,30), (60,90), (20,50)]
print(list(zip(*l)))
 
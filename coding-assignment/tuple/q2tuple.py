# Write a Python program to add an item in a tuple

# Sample Output

# (10, 40, 50, 70, 90)

# add items in list = 20

# (10, 40, 50, 70, 90, 20)
t = (10,40,50,70,90) 
print(t)
t = t + (20,)
print(t)
l = list(t) 
l.append(30)
t = tuple(l)
print(t)
# Write a Python program to create the colon of a tuple

# Sample Output

# ("Tutor", 'J', 23 , 56.67 , [23,12] , True)

# Copy = ('Tutor', 'J', 23, 56.67, [23, 12], True)
from copy import deepcopy
#create a tuple
t = ("Tutor", 'J', 23 , 56.67 , [23,12] , True) 
print(t)
#make a copy of a tuple using deepcopy() function
tc = deepcopy(t)
tc[4].append(50)
print(tc)
print(t)
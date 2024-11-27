# Write a program to get the maximum and minimum value of dictionary.

# Sample Output

# Dictionary = { "m1" : 78 , "m2" : 89 , "m3" : 64 , "m4" : 35 , "m5" : 71 }

# Maximum = 89

# Minimum = 35
marks={"m1":78 , "m2":89 , "m3":64 , "m4":35 , "m5":71}
 
v = marks.values()
maxi = max(v)
mini = min(v)
 
print("Maximum :",maxi)
print("Minimum :",mini)
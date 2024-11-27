# Write a program to sum all the values of a dictionary.

# Sample Output

# Dictionary = { "m1" : 92 , "m2" : 56 , "m3" : 88 , "m4" : 97 , "m5" : 89 }

# Sum of Values = 422

marks={"m1":92 , "m2":56 , "m3":88 , "m4":97 , "m5":89}
total = []
 
for i in marks.values():
	total.append(i)
 
print("Sum of Values :",sum(total))
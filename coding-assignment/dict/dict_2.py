
# 3. Write a Python program to concatenate following dictionaries to create a new one.

# Sample Output

# Dictionary 1 = {"Name" : "Ram" , "Age" : 23}

# Dictionary 2 = {"City" : "Salem", "Gender" : "Male"}

# Concatenate Dictionaries = {'Name' : 'Ram', 'Age' : 23, 'City' : 'Salem', 'Gender': 'Male'}

d1={"Name":"Ram" , "Age":23}
d2={"City": "Salem", "Gender": "Male"}
d3={"Mark":450}
d4 = {}
for d in (d1, d2, d3): d4.update(d)
print(d4)
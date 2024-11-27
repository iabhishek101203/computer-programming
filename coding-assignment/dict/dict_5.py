# Write a Python script to merge two Python dictionaries.

# Sample Output

# {"Name" : "Ram" , "Age" : 23}

# {"City" : "Salem", "Gender" : "Male"}

# {'Name' : 'Ram', 'Age' : 23, 'City' : 'Salem', 'Gender' : 'Male'}

d1={"Name":"Ram" , "Age":23}
d2={"City": "Salem", "Gender": "Male"}
res = d1.copy()
res.update(d2)
print(res)
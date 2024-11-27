# Write a Python program to Merge two Python dictionaries into one

# Sample Output

# {"Name" : "Ram" , "Age" : 25 , "City" : "Salem"}

# {"Gender" : "Male" , "Mark" : 422 , "Percent" : 84.4}

# {'Name' : 'Ram', 'Age' : 25, 'City' : 'Salem', 'Gender' : 'Male', 'Mark' : 422, 'Percent' : 84.4}

keys = ["One", "Two", "Three", "Four", "Five"]
values = [1, 2, 3, 4, 5]
 
res = dict(zip(keys, values))
print(res)
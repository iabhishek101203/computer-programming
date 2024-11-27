#  Write a Python program to Initialize dictionary with default values

# Sample Output

# [ "Siva", "Sam" ]

# { "designation" : "Student", "Department" : "BCA" }

# { 'Siva': {'designation' : 'Student', 'Department' : 'BCA'}, 'Sam': {'designation' : 'Student', 'Department' : 'BCA'} }

# Siva : {'designation' : 'Student', 'Department' : 'BCA'}

# Sam : {'designation' : 'Student', 'Department' : 'BCA'}

stu = ["Siva", "Sam", "Ram", "Pooja"]
defaults = {"designation": "Student", "Department": "BCA"}
 
result = dict.fromkeys(stu, defaults)
print(result)
 
# Individual data
print("\nSiva :",result["Siva"])
print("\nSam :",result["Sam"])
print("\nRam :",result["Ram"])
print("\nPooja :",result["Pooja"])
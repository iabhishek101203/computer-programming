#  Drop empty Items from a given Dictionary

# Sample Output

# Before Dropping = {'Name' : 'Pooja', 'Age' : 23, 'Gender' : None, 'Mark' : 488, 'City' : None}

# After Dropping = {'Name' : 'Pooja', 'Age' : 23, 'Mark' : 488}

student = {"Name": "Pooja", "Age":23, "Gender": None, "Mark":488, "City": None}
print("Before Dropping :",student)
student = {key:value for (key, value) in student.items() if value is not None}
print("After Dropping :",student)
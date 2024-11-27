#  Write a Python program to Delete a list of keys from a dictionary

# Sample Output

# Dictionary = {"Name" : "Tara", "RollNo" : 130046, "Mark" : 450, "Age" : 16, "Gender" : "Female", "City" : "Salem"}

# Keys to remove From a Dictionary = ["Gender", "City"]

# After Delete Dictionary = {'Name' : 'Tara', 'RollNo' : 130046, 'Mark' : 458, 'Age' : 16}

student = {
	"Name": "Tara",
	"RollNo":130046, 
	"Mark": 458, 
	"Age":16,
	"Gender":"Female",
	"City": "Chennai"
}
print("Before Delete :",student)
# Keys to remove From a Dict
keys = ["Gender", "City"]
 
for k in keys:
    student.pop(k)
print("After Delete :",student)
# Write a program to print values of dictionary.

# Sample Output

# Dictionary = {"Name": "Tara", "RollNo":130046, "Mark": 450, "Age":16, "Gender":"Female", "City": "Salem"}

# Dictionary Values
# Tara
# 130046
# 450
# 16
# Female
# Salem

student = {
	"Name": "Tara",
	"RollNo":130046, 
	"Mark": 458, 
	"Age":16,
	"Gender":"Female",
	"City": "Chennai"
}
print(student.values())
print("\n==== Values ====")
for v in student.values():
	print(" ",v)
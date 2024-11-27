# Write a Python program to check multiple keys exists in a dictionary.

# Sample Output

# Dict = { 'name' : 'Ram', 'age' : 23, 'city' : 'Salem' }

# Keys = {'age', 'name'}

# keys exists in a dictionary : True

# Keys = {'city', 'Salem'}

# keys exists in a dictionary : False
student = {
  'name': 'Ram',
  'age': 23,
  'city': 'Salem'
}
print(student.keys() >= {'age', 'name'})
print(student.keys() >= {'City', 'Ram'})
print(student.keys() >= {'city', 'Salem'})

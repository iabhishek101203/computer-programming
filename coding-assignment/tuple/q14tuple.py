# Write a Python program to convert a list of tuples into a dictionary

# Sample Output

# [ ("Name", "Ram"), ("Name", "Pooja"), ("Age", 21), ("Gender", "Male"), ("Age", 23), ("Gender", "Female") ]

# { 'Name' : ['Ram', 'Pooja'], 'Age' : [21, 23], 'Gender' : ['Male', 'Female'] }

l = [("Name", "Ram"), ("Name", "Pooja"), ("Name", "Sara"), ("Age", 21), ("Gender", "Male"), ("Age", 23), ("Gender", "Female"), ("Gender", "Female") , ("Age", 22)]
dic = {}
for x, y in l:
    dic.setdefault(x, []).append(y)
print (dic)
 
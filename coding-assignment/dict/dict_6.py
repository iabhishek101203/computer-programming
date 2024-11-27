# .Write a Python program to iterate over dictionaries using for loops.

# Sample Output

# {"Name" : "Ram" , "Age" : 23 , "City" : "Salem", "Gender" : "Male"}

# Name : Ram

# Age : 23

# City : Salem

# Gender : Male

d={"Name":"Ram" , "Age":23 , "City": "Salem", "Gender": "Male"}
for k, v in d.items():
     print(k, ' : ', d[k])      
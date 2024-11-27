#  Write a Python program to Replace words from Dictionary

# Sample Output

# String = Tutor joe's Computer Education

# Replaced Strings = Tutor joe's Software Solution

val = "Tutor joe's Computer Education"
print("Original string : ",val)
 
dic = {"Computer" : "Software ", "Education" : "Solution"}
 
word = val.split()
res = []
for w in word:
	res.append(dic.get(w, w))	
res = ' '.join(res)
 
print("Replaced Strings : " ,res)
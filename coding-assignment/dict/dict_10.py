# Match key values in two dictionaries

# Sample Output

# A = {'Tamil' : 92, 'English' : 56, 'Maths' : 88, 'Sceince' : 97, 'Social' : 89}

# B= {'Tamil' : 78, 'English' : 68, 'Maths' : 88, 'Sceince' : 97, 'Social' : 56}

# Maths : 88 is present in both A and B

A = {'Tamil': 92, 'English': 56, 'Maths': 88, 'Sceince': 97, 'Social': 89}
B= {'Tamil': 78, 'English': 68, 'Maths': 88, 'Sceince': 97, 'Social': 56}
for (key, value) in set(A.items()) & set(B.items()):
    print('%s: %s is present in both A and B' % (key, value))
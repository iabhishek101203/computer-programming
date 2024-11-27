# Write a Python program to remove duplicates from a list

# Sample Output

# [1,2,3,7,2,1,5,6,4,8,5,4]

# {1,2,3,4,5,6,7,8}

a = [1,2,3,7,2,1,5,6,4,8,5,4]
dup = set()
uniq = []
for x in a:
    if x not in dup:
        uniq.append(x)
        dup.add(x)
print(dup)
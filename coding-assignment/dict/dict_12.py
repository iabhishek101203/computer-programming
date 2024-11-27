# Write a Python program to print a dictionary line by line.

# Sample Output

# Dict = {  "Sam" : {"M1" : 89, "M2" : 56, "M3" : 89},
#                "Suresh" : {"M1" : 49, "M2" : 96, "M3" : 89} }

# Sam
# M1 : 89
# M2 : 56
# M3 : 89
# Suresh
# M1 : 49
# M2 : 96
# M3 : 89

sub = {"Sam":{"M1":89,"M2":56,"M3":89},
        "Suresh":{"M1":49,"M2":96,"M3":89}}
for a in sub:
    print(a)
    for b in sub[a]:
        print (b,":",sub[a][b])
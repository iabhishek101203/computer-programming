# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

# Sample Output

# Enter the Limit : 5

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
l=int(input("Enter the Limit : "))
d = dict()
 
for x in range(1,l+1):
    d[x]=x*x
print(d) 
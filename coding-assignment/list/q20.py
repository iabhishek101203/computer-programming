# Write a Python program to find the second smallest number in a list

# Sample Output

# [2,4,56,78,4,34,5,8,9]

# Second Smallest Number : 4
num = [ 2,4,56,78,4,34,5,8,9]
if (len(num)<2):
  print(num)
if ((len(num)==2)  and (num[0] == num[1]) ):
  print(num)
dup_items = set()
uniq_items = []
for x in num:
  if x not in dup_items:
    uniq_items.append(x)
    dup_items.add(x)
uniq_items.sort()    
print(  uniq_items[1]   )
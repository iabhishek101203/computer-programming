n=input("enter the string")
vowel="aeiouAEIOU"
c=0
for char in n:
    if char in vowel:
        c=c+1
print(c)        
str=input("enter the string")
c=0
vowel="aeiouAEIOU"
for char in str:
    if char in vowel:
        c+=1
print(f"the number of vowels are {c}")        

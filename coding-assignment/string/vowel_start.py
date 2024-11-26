names = input("Enter names separated by spaces: ").split()
vowel_names = []
other_names = []
vowels = "AEIOUaeiou"
for name in names:
    if name[0] in vowels:
        vowel_names.append(name)
    else:
        other_names.append(name)
rearranged_names = vowel_names + other_names
print("Rearranged list of names:", rearranged_names)
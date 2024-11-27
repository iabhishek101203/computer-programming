# Enter the String = ComPuTeR

# Check if there are at least 2 uppercase letters in the first 4 characters = COMPUTER

# Enter the String = Computer

# Check if does not contain at least 2 uppercase letters in the first 4 characters = Computer
str = input("Enter the String :")
num_upper = 0
for letter in str[:4]: 
	if letter.upper() == letter:
		num_upper += 1
if num_upper >= 2:
	print(str.upper())
print(str)

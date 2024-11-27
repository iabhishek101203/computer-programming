# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '@', except the first char itself.

# Sample Output

# Given String = tutor joes

# After String = tu@or joes

str=input()
print("Given String :",str)
ch = str[0]
str = str.replace(ch, '@')
str = ch + str[1:]
print("After String :",str)
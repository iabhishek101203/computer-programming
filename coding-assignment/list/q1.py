# Question 1: Sort Strings by Length
# Scenario:
# A group of friends is organizing a list of words for a spelling contest. To prepare, they want to sort the words based on their lengths, with the shortest word first.

# Problem Description:
# Write a function to sort a list of strings by their lengths. If two strings have the same length, maintain their relative order as in the input list.

# Input Format:
# A single line containing space-separated strings.

# Output Format:
# A single line containing the sorted strings.

# Example:
# Input: apple banana fig date
# Output: fig date apple banana

def sort_strings_by_length(input_line):
    words = input_line.split()
    sorted_words = sorted(words, key=len)
    return " ".join(sorted_words)
input_line = input()
output = sort_strings_by_length(input_line)
print(output)

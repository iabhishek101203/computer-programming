`# Question 2: Group Strings by First Letter
# Scenario:
# A librarian wants to organize a list of book titles such that all titles starting with the same letter are grouped together.

# Problem Description:
# Given a list of strings, group the strings by their first letter, maintaining their original order within each group.

# Input Format:
# A single line containing space-separated strings.

# Output Format:
# Groups of strings, each starting with the same letter.

# Example:
# Input: apple banana apricot berry almond
# Output: [apple apricot almond] [banana berry]

from collections import defaultdict
def group_strings_by_first_letter(input_line):
    words = input_line.split()
    grouped = defaultdict(list)
    for word in words:
        first_letter = word[0].lower()  
        grouped[first_letter].append(word)
    result = []
    for key in sorted(grouped.keys()):  
        result.append(f"[{' '.join(grouped[key])}]")
    return " ".join(result)
input_line = "apple banana apricot berry almond"
output = group_strings_by_first_letter(input_line)
print(output)
`
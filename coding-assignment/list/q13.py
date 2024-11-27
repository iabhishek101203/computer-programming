
#  Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. (enumerate)

# Sample Output

# ["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]

# ['Dog', 'Elephant', 'Fox', 'Ponda']

animal = ["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]
animal = [x for (i,x) in enumerate(animal) if i not in (0,4,5)]
print(animal)
 
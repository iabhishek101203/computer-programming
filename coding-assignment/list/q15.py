# Write a Python program to shuffle and print a specified list (shuffle)

# Sample Output

# ["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]

# ['Fox', 'Cat', 'Tiger', 'Lion', 'Dog', 'Ponda', 'Elephant']
from random import shuffle
animal = ["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]
shuffle(animal)
print(animal)
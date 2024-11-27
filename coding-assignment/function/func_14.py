# Write three functions called addNumbers, subtractNumbers, and calculate. The function addNumbers should take two numbers (x and y) as parameters and return the value of adding them together, while subtractNumbers should also take two numbers (x and y) and return the value of x minus y. Lastly, define a function called calculate that takes three numbers (a, b, and c) and uses addNumbers and subtractNumbers to add a and b and subtract c. The value should be returned. For example, calculate(2,3,4) should return 1.
def addNumbers(x, y):

    # Return the value of adding x and y together
    return x + y

def subtractNumbers(x, y):
    # Return the value of subtracting y from x
    return x - y

def calculate(a, b, c):

    # Call addNumbers, passing in a and b as parameters, and set the answer equal to the variable result
    result = addNumbers(a, b)
    # Call subtractNumbers on the result of the addition and c, the un
    finalResult = subtractNumbers(result, c)
    # Returns the finalResult
    return finalResult
# Write a function called remainder that takes in parameters x and y (where y defaults to 4) and returns the remainder of x divided by y. Ignore cases for when x is negative or y is less than or equal to 0. For example, remainder(5) should return 1.
# Function headers end with a colon (:) and a default value for y
def remainder(x, y = 4):

    # Indent four spaces after the header
    # Use modulus division (%) instead of double slashes (//) to get the remainder
    z = x % y

    # Keyword return is lowercase and returns z (the remainder of x divided by y)
    return z
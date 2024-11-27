# Write a function called address that combines 3 different string address parameters (city, state, and zip) and returns a user’s address. After the city and state inputs, add a comma and a space. For example, address('Seattle', 'WA', '98105') should return "Seattle, WA, 98105"
def address(city, state, zip):
    user_address = city + ", " + state + ", " + zip
    return user_address
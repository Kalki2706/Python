# Whenever you create a variable in Python, it has a value with a corresponding data type.

# Integers
# numbers without any fractional part and can be positive or negative
# We can use type() function to know which type of data type is being used in code.

x = 14

print(x)
print(type(x))


# Floats 
# Floats are numbers with fractional parts. They can have many numbers after decimal.

nearly_pi = 3.141592653589793238462643383279502884197169399375105820974944

print(nearly_pi)
print(type(nearly_pi))

# We can also specify a float with a fraction. 

almost_pi = 22 / 7

print(almost_pi)
print(type(almost_pi))


# One function that is particularly useful for fractions is the round() function. It lets you round a number to a specified number of decimal places.

# Round to 5 decimal places

rounded_pi = round(almost_pi, 5)

print(rounded_pi)
print(type(rounded_pi))
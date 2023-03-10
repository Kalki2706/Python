# Whenever you create a variable in Python, it has a value with a corresponding data type.

# "INTEGERS"
# numbers without any fractional part and can be positive or negative
# We can use type() function to know which type of data type is being used in code.

x = 14

print(x)
print(type(x))


# "FLOATS"

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


# Pyhton recognizes float data type for ex. 1. or 1.0 , 1.00 etc. will be float even they don't have any fractional part

y_float = 1.

print(y_float)
print(type(y_float))


# "Booleans"

# Booleans print only True or False.
# z_one value given is true.
z_one = True 

print(z_one)
print(type(z_one))

z_two = False

print(z_two)
print(type(z_two))

# Booleans is used to represent the truth value of an expression. 

z_three = (1 < 2)

print(z_three)
print(type(z_three))


# Since 5 < 3 is false statement.
z_four = (5 < 3)

print(z_four)
print(type(z_four))


# Switch the value by using not. So not True is equivalent to False, & not False becomes True.

z_five = not z_four

# z_four is false but with not z_four it becomes true.
print(z_five)
print(type(z_five))

# "STRINGS"

# The string data type is a collection of characters (like alphabet letters, punctuation, numerical digits, or symbols) contained in quotation marks. Strings are commonly used to represent text.

w = "Hello, Python!"
print(w)
print(type(w))


# Len function in string to know the length of a string

name = "Kalki"

print(name)
print(len(name))


# One special type of string is the empty string, which has length zero.

shortest_string = ""

print(shortest_string)

print(type(shortest_string))
print(len(shortest_string))


# If you put a number in Quotation marks, it has a string data type

my_num = "1.12321"

print(my_num)

print(type(my_num))
print(len(my_num))


# If we have a string that is convertible to a float, we can use float().

# This won't always work! For instance, we can convert "10.43430" and "3" to floats, but we cannot convert "Hello, Python!" to a float.

also_my_num = float(my_num)

print(also_my_num)
print(type(also_my_num))


# Adding Strings

new_string = "abc" + "def"

print(new_string)
print(type(new_string))


# Note that it's not possible to do subtraction or division with two strings. You also can't multiply two strings, but you can multiply a string by an integer. This again results in a string that's just the original string concatenated with itself a specified number of times.

newest_string = "abc" * 3

print(newest_string)
print(type(newest_string))

# Added space after abc string to get space in output.

newest_string = "abc " * 3

print(newest_string)
print(type(newest_string))


# You can't multiply float with string
# Uncomment below code to check the error.

# will_not_work = "abc " * 3.
# print(will_not_work)

# Just checking if i can multiply without declaring a variable &&&.... It works! :)

print("hello " * 3)
# Arithmetic & Variables 

a = 1 
b = 2 
print(a + b)


var_a = 10
var_b = 10

print(var_a ** var_b)

var_y = 30
var_z = 10

print(var_y / var_z)


# Variable means name that we give to store data 
# var_a & var_b is a variable to store data.


# Data types

# Int - stores only number without fraction for eg. 1, 0, -1 

# float - stores only fraction number 1.0, -1.0

# boolean - True or false

# String - "kalki" stores text

# you can only add string with string

# You can only multiply string with int others will throw an error.

# Example 
# int
var_a = 100
var_b = 200

print(var_a + var_b)

# float

var_a = 10
var_b = 200

print(var_a / var_b)

# String

name = "Kalki"
print(name)


# String addition

name = "Kalki "
number = "2706"

print(name + number)

name = "Kalki "
number = "2706"
name_num = name + number

print(name_num)


# String multiply with int

name = "Kalki "
output = name * 3

print(output)


# Booleans

var_a = True
var_b = False

print(var_a)
print(type(var_a))

# The value of true is 1
var_a = "Kalki"

var_b = True

var_c = False

print(len(var_a) + var_b)
print(var_b + var_c)


# multiplying int with float

number = 10
number_with_fraction = 10.0

print(number * number_with_fraction)

# Using def to multiply int and float

def get_number(number, number_with_fraction):
    # multiplying numbers by taking input
    total = number * number_with_fraction

    return total

output = get_number(10, 5.4)
print(output)
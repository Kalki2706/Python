# Question 1
# Define a float 

y = 1.

print(y)
print(type(y))

# Convert float to integer with the int function

z = int(y)

print(z)
print(type(z))

# Question 2

print(3 * True)

print(-3.1 * True)

print(type("abc" * False)) 

print(len("abc" * False))

name = "abc " * False
print(name)

# When you multiple an integer or float by a boolean with value True, it just returns that same integer or float (and is equivalent to multiplying by 1). If you multiply an integer or float by a boolean with value False, it always returns 0. This is true for both positive and negative numbers. If you multiply a string by a boolean with value True, it just returns that same string. And if you multiply a string by a boolean with value False, it returns an empty string (or a string with length zero).


# Question 3
# Solved by me without seeing the solution & the answer is right
def get_expected_cost(beds, baths, has_basement):
    value = 80000 + beds * 30000 + baths * 10000 + has_basement * 40000
    return value

total_cost = get_expected_cost(1, 1, True)
print(total_cost)
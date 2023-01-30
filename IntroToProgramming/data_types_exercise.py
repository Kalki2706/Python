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


# Question 4
# In below codes the false is equivalent to 0 and true is equal to 1 

print(False + False)
print(True + False)
print(False + True)
print(True + True)

# False is 0 and true is 1 = (0 + 1 + 1 + 1)
print(False + True + True + True)


# Question 5
# You own an online shop where you sell rings with custom engravings. You offer both gold plated and solid gold rings.
# 1) Gold plated rings have a base cost of $50, and you charge $7 per engraved unit.
# 2) Solid gold rings have a base cost of $100, and you charge $10 per engraved unit.
# 3) Spaces and punctuation are counted as engraved units.

def cost_of_project(engraving, solid_gold):
    cost = solid_gold * (100 + 10 * len(engraving)) + (not solid_gold) * (50 + 7 * len(engraving))
    return cost

# solid gold = true
project_one = cost_of_project('Charlie+Denver', False)
print(project_one)

# not solid gold = false
project_two = cost_of_project("08/10/2000", False)
print(project_two)
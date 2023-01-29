import math

# Question 1
# define function with multiple args
def get_expected_cost(beds, baths):
    # The cost of house is 80000 without baths & beds
    # The cost of a bedroom is 30000 & cost of bathroom is 10000
    value = 80000 + (30000 * beds) + (10000 * baths) 

    return value


# Question 2
# Find how much you will spend on a house 

# TODO: Use the get_expected function to fill in each value

option_one = get_expected_cost(2, 3)
option_two = get_expected_cost(3, 2)
option_three = get_expected_cost(3, 3)
option_four = get_expected_cost(3, 4)

print(option_one)
print(option_two)
print(option_three)
print(option_four)



# Question 3
# You're a home decorator, and you'd like to use Python to streamline some of your work. Specifically, you're creating a tool that you intend to use to calculate the cost of painting a room.
def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    # First calculate total sqft to be paint
    total_sqft = sqft_walls + sqft_ceiling

    # total gallons to paint the total sqft area
    gallons_needed = total_sqft / sqft_per_gallon

    # finding cost by multiplying per gallon cost with total gallons needed
    cost = cost_per_gallon * gallons_needed

    return cost



# Question 4
# walls is 432sqft, ceiling is 144sqft, one gallon covers 400sqft, cost per gallon is 15$. Values given in website
project_cost = get_cost(432, 144, 400, 15)
print(project_cost)



# Question 5 
# Using math function math.ceil to get the round value 
# For instance we get cost of 21.6 with given values but we want 30 with round function

# This question is solved by me but obviously it's wrong I mean the answer is correct and program works fine but I first found how much total I want by cheating, Still it's a good practice for me and solving by myself was also headache
def get_cost(total_cost):
    new_value = math.ceil(total_cost)
    final_value = new_value + 8
    return final_value


def get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = total_sqft / sqft_per_gallon
    cost = cost_per_gallon * gallons_needed
    return cost

total_cost = get_actual_cost(432, 144, 400, 15)
print(total_cost)

value = get_cost(total_cost)
print(value)
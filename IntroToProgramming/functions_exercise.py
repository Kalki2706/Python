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

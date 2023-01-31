# Conditions & Conditional Statements

# Conditions are based on if else statement & It's a boolean type. If the condition is true it will print the true value else the condition will print false

a = 2 > 3

print(a)
print(type(a))

# Function that will add any number with 5
def add_five(num):
    ans = 5 + num 
    return ans

answer = add_five(7)
print(answer)

# But in above code we can't do something like if the number is less than 10 it will add 3 and if number is more than 10 it will add 8 for that we need conditions.abs(x)


# Using variables to compare the conditions 

var_one = 1
var_two = 2

print(var_one < 1)
print(type(var_one))

# Commom symbols you can use to construct conditions
# == equals, != does not equal, < less than
# <= less than equal, > greater than, >= greater than equal

var_one == 1
print(var_one)

# Conditional statements use conditions to modify how your function runs. They check the value of a condition, and if the condition evaluates to True, then a certain block of code is executed. (Otherwise, if the condition is False, then the code is not run.


# "if" statement 

def evaluate_temp(temp):
    # Set an initial message
    message = "Normal temprature."

    # Update value of message only if temprature greater than 38
    if temp > 38:
        message = "Fever!"

    return message

fever = evaluate_temp(40)
print(fever)

# We can call function without declaring variable
# print(evaluate_temp(38))
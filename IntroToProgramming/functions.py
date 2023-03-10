# Defining a function: def - define 

# Def is a function and add_three is a function name and inside parentheses arugument is passed for taking input and ends with colon : The def line comes under HEAD SECTION
def add_three(input_var):

    # output var is gonna give output by adding 3 in input variable AFTER THE COLON EVERYTHING UNDER DEF IS BODY SECTION
    output_var = input_var + 3

    # return is a keyword which is gonna return the value of output var
    return output_var

# When we run a function, it can also be referred to as "calling" the function.

# declared new_num variable to ouput & the input var added value in add_three def 
new_num = add_three(10)

# Printing value by adding input_var + 3 which will be 13
print(new_num)



# Complex Example 
# Solved by me
# def get_pay(num_hours):
#     pay_pretax = num_hours * 15

#     tax = (pay_pretax * 12/100)

#     pay_aftertax = pay_pretax - tax

#     return pay_aftertax

# pay_fulltime = get_pay(40)
# print(pay_fulltime)


# pay_parttime = get_pay(32)
# print(pay_parttime)


# Complex Example 
# Solved by the website

def get_pay(num_hours):
    pay_pretax = num_hours * 15

    # 1 - 0.12 is 0.88 and multiply it with pay_pretax variable
    pay_aftertax = pay_pretax * (1 - 0.12)

    return pay_aftertax

# Working 8 hours a day for 5 days per week
pay_fulltime = get_pay(40)
print(pay_fulltime)

# Working 6.4 hours a day for 5 days per week
pay_parttime = get_pay(32)
print(pay_parttime)




# Variable Scope
# Variables defined inside the function body cannot be accessed outside of the function. For example trying to print variable of above code which is under def function

# Uncomment the below code to see the error
# print(pay_aftertax)

# Variables under def function have a LOCAL SCOPE & Variables outside of def function have a GLOBAL SCOPE



# Functions with multiple arguments
# Solved by me without seeing tried myself beforhand

# def get_pay_with_more_inputs(num_hours, hourly_wage, tax_bracket):
#     pay_pretax = num_hours * hourly_wage

#     pay_aftertax = pay_pretax * (1 - tax_bracket)

#     return pay_aftertax


# higher_pay_aftertax = get_pay_with_more_inputs(40, 15, .12)
# print(higher_pay_aftertax)


# Solved on website with different values
def get_pay_with_more_inputs(num_hours, hourly_wage, tax_bracket):
    pay_pretax = num_hours * hourly_wage

    pay_aftertax = pay_pretax * (1 - tax_bracket)

    return pay_aftertax

higher_pay_aftertax = get_pay_with_more_inputs(40, 24, .22)
print(higher_pay_aftertax)



# Functions with no arguments

# Define the function with no arguments and with no return
def print_hello():
    print("Hello, World!")
    print("Good morning")

# Call the function
print_hello()
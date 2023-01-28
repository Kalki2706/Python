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
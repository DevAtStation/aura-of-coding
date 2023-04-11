# Now lets talk about getting values from functions, another way to reuse code
# Instead of just printing the result lets do a bunch of functions that do calculations and use the result of the functions as arguments for other functions
# to get the result of the functions we can use the 'return' keyword and to the right of if put what we want to return from the function
def add_two_numbers(a, b):
    sum = a + b
    return sum

# let's do the same but with multiplication
def multiply_two_numbers(a, b):
    # instead of adding them into and assign them to a variable we can save a line and a variable and just return the operation
    return a * b

# Now lets call the first one
add_two_numbers(3, 2)
# this as you see, does nothing, we need to store the value that is returned somewhere, let's use a variable for that
result = add_two_numbers(3, 2)
# Now the result variable is storing the returned value from the function (5 in this case)
# we can use that value now to call the 2nd one and store it in the same variable, this may seem confusing but is really easy to follow
# We first use result as a parameter for the next function like this 'multiply_two_numbers(result, 5)' since result is 5 and 5*5 is 25, the return value will need to be stored somewhere, we can use the same result variable for that
result = multiply_two_numbers(result, 5)
# now result should be storing the number 25, lets print it and be sure
print(f"The result is: {result}")
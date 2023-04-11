# functions are a way to reuse code, lets say you want to run something that prints a bunch of things multiple tines, you can define a function by using the 'def' keyword, followed by a name and a list of parameters, in this case we wont need parameters so we simply follow it by an empty group of parenthesis and a colon '():'
def print_a_lot():
    # also for things to be INSIDE the function they need to have the same indentation, in this case 4 spaces (just pressing the tab button will do) 
    print("FIRST LINE")
    # if we put an 'f' in front of the string we can also print values an variables buy putting them in brackets, for example we print the value 0 here 
    print(f"Printing {0}")
    # Let's print now a variable to make it mor interesting
    hard_calculation = 765 * 453
    print(f"Printing {hard_calculation}")
    # we can also do this trick in string variables
    hard_division = f"last number divided by 2 {hard_calculation/2}"
    print(f"Printing {hard_division}")
    print("LAST LINE")

# now to call a function we simply use the name of the function OUTSIDE the function, if we remove the indentation we should be outside the function (in this case 0 spaces)
print_a_lot()
# and as I said, this is practical to reuse code, so we dont need to define the prints again if we want to use the function again, we just call it again how many times we need
print_a_lot()
print_a_lot()

# as I said functions can also have parameters, parameters are variables that are sent via arguments when we call said function, these are used to make functions more flexible, for instance, let's make a function that adds two numbers and prints them
# In the next line we have 2 variables, a and b, in between the parenthesis, we dont know what they are but let's assume they are two integers (whole numbers)
def add_and_print(a, b): 
    # as long as the 2 values are numbers, they can be added, you can perform many operation just with variables, we will use '+' to add 2 variables and store it into a new one called sum
    sum = a + b
    # And let's print the sum
    print(sum)

# And now let's call this function again from outside
add_and_print(4, 10)
# and we can reuse it with different numbers
add_and_print(42, 54)
# we could technically send different things but it would have unexpected behaviors, for example lets try adding two strings
add_and_print("Hello", "World")
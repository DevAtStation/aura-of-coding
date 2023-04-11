# if statements are used to control the flow of the code, to be a programmer you dont need only to know logic, you need to bend logic to your will, and the 'if' keyword will help you with that
# lets make an easy example, the 'if' keyword is used like this, "if 'condition':" and if the condition is met, then whats inside the if is executed. For instance let's use the 'less than' operator '<' to ask if a number is less than another:
if 1 < 3:
    print("1 is les than 3... no shit")
if 5 < 3:
    print("this will NEVER EVER execute")

# Now lets use ifs in a function and see how flexible it is, lets make a function that if the number is less than 10 it gets multiplied by 10 and if not it just returns the same number
def multiply_if_below_ten(x):
    if x < 10:
        x  = x * 10
    return x

# Lets organize the code output a bit more, by adding a '\n' at the start of the print to print an empty line and then lets add some sort of title to separate it from the last part of the code.
print("\nmultiply_if_below_ten calls:")
print(multiply_if_below_ten(5))
print(multiply_if_below_ten(15))
print(multiply_if_below_ten(-5))


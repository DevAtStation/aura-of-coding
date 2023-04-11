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

# Let's try using ifs to get different values from a function depending on the input, we will use if, elif and else for this and a few new operators
def guess_the_number():
    # here we use the input function (another python function like print) to get a number typed by the user when we call this function, this will be defined on runtime so is always the same as in other examples.
    guessed_number = input("Guess a number: ") # we take the number typed by the user and store it into guessed_number so we can use it later
    # Sadly user inputs in python are always assumed that they are strings, so we need to convert it to a number, after all we want to operate with numbers and not words or characters. To do this we just use the int() function that python provides to change the type of value that is inside guessed_number from a string to an int (integer, whole number)
    guessed_number = int(guessed_number)
    # We will say that the correct number is 420 just because, to do that we will ask if guessed_number is equal to 420, to do that we will use the equal operator, represented by '==' we use two '=' for this because the single one is reserved for variable assignations.
    if guessed_number == 420:
        # Let's just print CORRECT if the user guessed the number
        print("CORRECT")
    # now we can use the elif keyword to ask another thing, the flow goes like this, if the first if condition triggers, the rest of the elif statements wont be executed, but if the condition isn't met it will ask the next elif if the condition is met and so on (you can have infinite elif's). Here the condition is if guessed_number is greater than 420 this condition will be met, we use the '>' operator for greater than.
    elif guessed_number > 420:
        # if this is met lets give the user a hint that the correct number should be lower
        print("Guess lower")
    # And lastly else, else is triggered automatically when neither the if or non of the elif's statements conditions are met, in this case we assume that if the guessed_number is bellow 420 the else will trigger
    else:
        # one last hint
        print("Guess higher")
    
print("\guess_the_number calls:")
# Let's give the user 3 tries to guess
guess_the_number()
guess_the_number()
guess_the_number()

# Exercise 1.3: code a function named is_even that has one int parameter, and use the % operator to return a boolean (true if even, false if odd).


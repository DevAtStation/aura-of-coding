# Loops are a way to call parts of your code repeatedly while a condition is met or a certain number of times when you know how many times you need to call it.

# Let's start with the while loop, while loops work this way, we use the keyword 'while' and we add a condition after it between parenthesis. All the code inside the while block of code will continue executing while the condition is met, if not  it just will skip it and continue the normal flow.
# In this function will ask the user for input until he inputs 'HELP'
def while_demonstration():
    # we initialize user_input as an empty string to use it in the following lines, where possible try defining and initializing variables at the start of functions. We generally use 0 for numbers, false for booleans and "" for strings but your function may require different things, don't take this a hard rule, in our case anything except "EXIT" will work.
    user_input = ""
    # We use the data in the user input and we compare it with "EXIT", the operator '!=' is used for not equal, so we can translate this part of code to "while user_input is not equal to "EXIT" execute the following code" 
    while(user_input != "EXIT"):
        # We ask user for input, to use double quotes '"' inside strings we use \ before them so python knows we want to put more characters after it. 
        user_input = input("Type \"EXIT\" to exit: ")

# Never forget to call functions
while_demonstration()

# now for the next demonstration let's try integrating the while loop into the game we made earlier... but since we don't want to copy the code over lets use the 'from' and 'import' keywords, with them we can use functions from other files by writing the name of the file and then the name of the function we want to import. 
from _5_if_statements import guess_the_number

# We can also import ALL functions of a file the following way
#import _5_if_statements
# but if we do it this way we need to write the filename before using the function, like this:
#_5_if_statements.guess_the_number()

# Ok, this will be our function
def while_integration():
    # Since we made it so guess_the_number returns a boolean (true or false), we can use that boolean as a condition and in this case the code would translate to "while the return value of guess_the_number is false (we do this with the not), execute the following code"
    while(not guess_the_number()):
        # here we just use the 'pass' keyword to nothing and loop again, code blocks inside the while require  at  least to put 1 line of code and we dont really want to print anything here as all the printing is done on the function side.
        pass

# We call this one now
# while_integration()
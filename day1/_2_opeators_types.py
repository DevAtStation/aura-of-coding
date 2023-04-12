# As I said before we have the '=' operator that assigns data to a variable, but we also have normal math operators that we can apply to numbers a variables
x = 1 + 2 # the '+' operator adds values, in this case it will add 1 to 2 and store the result (3) into x
print(x)
x = x * 4 # the '*' operator multiplies values, in this case it will multiply the contents of x (in this case 3) by 4, and store the result (12) into x again
print(x)
y = x - 10 # the '-' operator subtracts values, in this case it will take the 12 inside x and subtract 10, storing the result (2) int a new variable, y, preserving the value in x
print(y)
z = x / y # the '/' operator divides values, in this case it will take the 12 inside x and divided by the x inside y, and store the result (6) into a new variable z
print(z)
# and the last important math operator is a weird one, this is the mod operator represented by '%', it gives you the remainder of a division, really useful to detect even or odd numbers or to limit the range of a number
z = x % 7 # this will take the 12 inside x and divide it by 7 and instead of giving you the result of the division (1.715~) it will give you the remainder (5) and store it in z
print(z)

# Now lets talk a bit about variable types, we already saw ints (whole numbers) and strings (words, chain of characters or letters), we can see if we pay attention to the print on the division result print, that there is a 6.0 instead of just 6, this is because when you make divisions python assumes you are using floats (floating point numbers, or another way to say numbers with decimals), after all it's safe to assume that most divisions will have decimals as a result.
# so we now know ints, strings and floats but one of the most important ones is booleans (true or false values), lets print an example
bool_value = True
print(bool_value)
bool_value = False
print(bool_value)
# these are simple on/off values that that require little memory and are really useful to store result from conditions and work pretty well with the 'if' statements that we will learn later
# another cool thing about booleans, is that you cna operate in weird ways, here we can use the 'not' keyword to negate the value of a boolean, in other words, if the boolean is true it will convert it to false and if false convert it to true.
bool_value = not bool_value
print(bool_value)
# moar cool things with booleans, you cna just assign statements to booleans and the boolean will be true if the statement, is true and false otherwise, is like asking a question and assigning the resulting "yes or no" to the variable, lets try an example
bool_value = 3 == 3 # here we are using the '==' (double equal) operator to ask if "is 3 equal to 3?", if true the true value will go into the variable, if not it will assign the false value to the variable. We can't use the '=' to ask if something is equal to another thing as the '=' operator is only used to assign a value on the right side to a variable on the left
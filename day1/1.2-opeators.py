# As I said before we have the '=' operator that assigns data to a variable, but we also have normal math operators that we can apply to numbers a variables
x = 1 + 2 # the '+' operator adds values, in this case it will add 1 to 2 and store the result (3) into x
print(x)
x = x * 4 # the '*' operator multiplies values, in this case it will multiply the contents of x (in this case 3) by 4, and store the result (12) into x again
print(x)
y = x - 10 # the '-' operator subtracts values, in this case it will take the 12 inside x and subtract 10, storing the result (2) int a new variable, y, preserving the value in x
print(y)
z = x / y # the '/' operator divides values, in this case it will take the 12 inside x and divided by the x inside y, and store the result (6) into a new variable z
print(z)
# and the last important math operator is a weird ona, this is the mod operator represented by '%', it gives you the remainder of a division, really useful to detect even or odd numbers or to limit the range of a number
z = x % 7 # this will take the 12 inside x and divide it by 7 and instead of giving you the result of the division (1.715~) it will give you the remainder (5) and store it in z
print(z)
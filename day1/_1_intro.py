# Let's start with the basic syntax

# '#' symbol is used to comment code like this part, this line of code will get ignored by python

# 'variables' a variable is a named piece of memory that stores data, for instance on the next line I will store an string (sequence of characters) into a variable, we do this by using the '=' operator, like 'variable = data'
title = "Aura of Coding"
# we can change variables to store different data
title = "Coding Aura"
# now title will store "Coding Aura" and the previous value is lost to the void
# we can also assign variables to other variables
newTitle = title
# now before changing the value of title, we store it in another variable, so we don't lose the value later if we need it 
title = "Aura of Coding"

# 'print()' print is a python function that will print into the terminal whatever is inside the (), it could be any value, like a number, a string or even what's inside variables (think of the terminal as a linux terminal that you see in hacker shows)
# Let's try printing our previous variables one after the other and a simple string
print("Hello Aura")
print(title)
print(newTitle)

# Now lets try running this by typing "python .\day1\_1_intro.py" on the terminal and hitting enter, also F5 on visual studio code runs the current python file
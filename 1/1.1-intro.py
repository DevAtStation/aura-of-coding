# Let's start with the basic syntax

# '#' simbol is used to comment code like this part, this line of code will get ignored by python

# 'variables' a variable is a named piace of memory that stures data, for example on the next line I will store an string (sequence of characters) into a variable
title = "Aura of Coding"
# we can change variables to store diferent data
title = "Coding Aura"
# now title will store "Coding Aura" and the previuous value is lost to the void
# we can also asign variables to other variables
newTitle = title
title = "Aura of Coding"
# now before changing the value of title, we store in another variable, so we dont loose the value if we need it later 

# 'print()' print is a python function that will print into the terminal whatever is inside the () it could be any value, like a number, a string or even what's inside variables (think of the terminal as a linux terminal that you see in hacker shows)
# Lets try printint our previous variables one after the other and a simple string
print("Hello Aura")
print(title)
print(newTitle)
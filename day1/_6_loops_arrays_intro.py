# Loops are a way to call parts of your code repeatedly while a condition is met or a certain number of times when you know how many times you need to call it.

# Let's start with the while loop, while loops work this way, we use the keyword 'while' and we add a condition after it as we did with the 'if' before. All the code inside the while block of code will continue executing while the condition is met, if not  it just will skip it and continue the normal flow.
# In this function will ask the user for input until he inputs 'HELP'
def while_demonstration():
    # we initialize user_input as an empty string to use it in the following lines, where possible try defining and initializing variables at the start of functions. We generally use 0 for numbers, false for booleans and "" for strings but your function may require different things, don't take this a hard rule, in our case anything except "EXIT" will work.
    user_input = ""
    # We use the data in the user input and we compare it with "EXIT", the operator '!=' is used for not equal, so we can translate this part of code to "while user_input is not equal to "EXIT" execute the following code" 
    while user_input != "EXIT":
        # We ask user for input, to use double quotes '"' inside strings we use \ before them so python knows we want to put more characters after it. 
        user_input = input("Type \"EXIT\" to exit: ")

# Never forget to call functions
# while_demonstration()

# We can also use while to count things, but the next loop type is better suited for it, here is an example with while kist to make the point
def while_counting():
    # we create a count variable and we start it as 0
    count = 0
    # and we increment it while is less than 10 
    while count < 10:
        # we print the value of count
        print(f"Count is: {count}")
        # we add 1 to count, using the '+=' operator, this is a short way to do this "count = count + 1" 
        count += 1
    # After count reaches 10 the condition wont be met and the while will stop executing and it will skip to this line
    print("Counting finished")

# Calling the counting function
# while_counting()

# As I said, we can use while for counting but the 'for' keyword is better for that.
def for_counting():
    # 'for' works this way, we write 'for' followed by a new variable that will be recycled on each loop, and then we use the keyword 'in' and something to be stored on the variable on each loop, in this case a we use the 'range' python function and we specify a range that goes from 0 to 10 (10 not included)
    for index in range(10): # range assumes we start at 0 always unless we specify it, "range(10)" is equal to "range(0, 10)"
        # in each loop 'index' with change values for each value on the range, starting on 0, then 1 and all the way to 9, when it reaches 10 it ends the loop.
        print(f"The value of the index is {index}") 

# function call
# for_counting()

# here we do the same but we change the range numbers to start at 10 instead of 0, and the index will change to 10, 11, 12, 13 and 14 in each loop
def for_counting2():
    for index in range(10, 15):
        print(f"The value of the index is {index}")

# function call
#for_counting2()


# here we do the same but we change how much we add in between loops, in this example index will start at 2, and since each loop adds 3, the next loop index will be 5, then 8 and when we add 3 more we go over 10 so the loops ends with 8 as the final index.
def for_counting3():
    for index in range(2, 10, 3):
        print(f"The value of the index is {index}")

# function call
#for_counting3()

# Aside from counting we can also use 'for' to iterate throw data, an string is just characters one after the other, so we can think that strings are a collection  of characters, you know what is great to go through collections and executing code? 'for' loops
def for_string():
    # word is based
    word = "based"
    # now instead o using a range we just put an string (or any other collection as I will show later) and in each loop 'letter' will be equal to a different letter of the word.
    for letter in word:
        print(f"The current letter is {letter}")

# func call
# for_string()

# We talked a bit about collections, arrays are the most basic types of collections, it's a variable that contains a list of data or other variables
# To make an array we create a variable as always and instead of assigning a single piece of data we assign multiple, we do this between square brackets and separated by a coma
# here is an example with numbers: "even_numbers = [2, 4, 6, 8]", in this example we have a variable that contains an array, and the array contains 4 values that are int, 
# To access these values we do it this way, we write the variable and we add brackets and the index of the position of the value, starting with 0 as the first position, for instance to access the value '6' in the array I declared before we need the value at the 3rd position and since we access the first position with the number 0 to access the 3rd we use the number 2, for example if we print "even_numbers[2]" it will output the value '6'
# let's try now iterating through an array of words
def for_array():
    # we declare a new variable and we assign an array to it, this time the array is an string array, and each word is a collection of characters so we can have collections inside collections (It's turtles all the way down)
    words = ["based", "chad", "red-pill"]
    # now we use 'word' as the new variable and each loop word a different word from the 'words' array will be assigned to word
    for word in words:
        #we print
        print(f"The current extremist word is {word}")

# we call
# for_array()

# now let's combine method 1 with method 2 of using for, we will use the 'range' func that we used before to get the numbers from 0 (start of the array), to 2 (end of the array), to get the number of elements in an array we can use the 'len' python function by writing the name of the array as an argument "len(array)" 
def for_array2():
    # we define the array of words
    words = ["based", "chad", "red-pill"]
    # we get te range that we need, in this case we need 'range(3)', but since we could add more elements (or remove), from an array, we don't want to go editing the range each time we touch the array, so we get the current length of the array with 'len'
    for index in range(len(words)):
        # we print again, but this time with the 'index' variable in between square brackets to specify which position we want to print in each loop,  as the index will change each loop, this will print all words. 
        print(f"The current extremist word is {words[index]}")

# we call again
# for_array2()

# And for the last demonstration we can skip elements in the array with the other range parameters, let's try that
def skip_cringe_words():
    # we define the array of words
    words = ["based", "cringe", "chad", "chud", "red-pill", "blue-pill"]
    # we now need to specify all 3 arguments of the range function so we can add how many numbers we want to add each loop
    for index in range(0, len(words), 2):
        # print
        print(f"The current extremist word is {words[index]}")
# call
#skip_cringe_words()

# we can also combine 'for's with code flow statement like the 'if' let's use that to skip all words equal to cringe
def skip_only_cringe():
    # we define the array of words
    words = ["based", "cringe", "chad", "red-pill"]
    # we do the same 'for' as in the 'for_array()' func we wrote before
    for word in words:
        # and now we ask, "is the current word not equal to cringe?" if this is true,  it will print, if not it will just loop again with a new word
        if word != "cringe":
            print(f"The current none cringe word is {word}")

#skip_only_cringe()

# last 'for' example (for now)
def skip_only_cringe2():
    # next few lines are the same
    words = ["based", "cringe", "chad", "red-pill"]
    for word in words:
        #here we ask the other way around "is the current word equal to cringe?" if so, it will enter the code inside the if
        if word == "cringe":
            # since we dont want to do anything with "cringe" we use the 'continue' keyword to skip the current loop to the next one, it wont print the next line as it will get skipped, 'continue' works for while loops too
            continue 
        print(f"The current none cringe word is {word}")

# never forgetti
# skip_only_cringe2()

# # now for the next demonstration let's try integrating the while loop into the game we made earlier... but since we don't want to copy the code over lets use the 'from' and 'import' keywords, with them we can use functions from other files by writing the name of the file and then the name of the function we want to import.
# from _5_if_statements import guess_the_number

# # We can also import ALL functions of a file the following way
# #import _5_if_statements
# # but if we do it this way we need to write the filename before using the function, like this:
# #_5_if_statements.guess_the_number()

# # Ok, this will be our function
# def while_integration():
#     # Since we made it so guess_the_number returns a boolean (true or false), we can use that boolean as a condition and in this case the code would translate to "while the return value of guess_the_number is false (we do this with the 'not'), execute the following code"
#     while not guess_the_number():
#         # here we just use the 'pass' keyword to nothing and loop again, pass just is a line that does nothing, can be used as a placeholder, but here, the code blocks inside the while require at least to put 1 line of code and we dont really want to print anything here as all the printing is done on the function side.
#         pass

# # We call this one now
# # while_integration()


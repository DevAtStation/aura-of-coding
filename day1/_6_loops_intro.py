#

def while_demonstration():
    user_input = ""
    while(user_input != "EXIT"):
        user_input = input("Type \"EXIT\" to exit: ")

# while_demonstration()

from _5_if_statements import guess_the_number

def while_integration():
    while(not guess_the_number()):
        pass

while_integration()
def if_refresh(condition1, condition2, condition3):
    if condition1:
         print("First condition was true and the function will return")
    elif condition2:
        print("Second condition was true")
    elif condition3:
        print("Third condition was true")
    else:
        print("None of the conditions were true and the function will return")
        return
    print("At least one of the conditions were true")

def if_complex(condition1, condition2, condition3):
    if condition1 or condition2 or condition3:
        print("At least one of the conditions were true")
    else:
        print("None of the conditions were true")

    if condition1 and condition2 and condition3:
        print("All of the conditions were true")
    else:
        print("At least one of the conditions was false")

    if condition1 or (condition2 and condition3):
        print("The first condition was true or all of the others were true")
    else:
        print("The first condition was false and at least one of the others were false")
    
    if condition1 and (condition2 or condition3):
        print("The first condition was true and at least one of the others were true")
    else:
        print("The first condition was false or at least one of the others were false")
    
if_refresh(True, True, True)
if_refresh(False, True, False)
if_refresh(False, False, True)
if_refresh(True, False, False)
if_refresh(False, False, False)

if_complex(True, True, True)
if_complex(False, False, False)
if_complex(True, True, False)
if_complex(False, False, True)
if_complex(True, False, False)
if_complex(False, True, True)
if_complex(True, False, True)
if_complex(False, True, False)

        
def guess_the_number(number):
    guessed_number = input("Guess a number: ")
    guessed_number = int(guessed_number)
    if guessed_number == number:
        print("CORRECT")
        return True 
    elif guessed_number > number:
        print("Guess lower")
    else:
        print("Guess higher")

    return False

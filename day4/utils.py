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

#from random import randint
#secret_number = randint(0, 9)


#### Sonjas code starts here #####

def read_number ():
    input_from_user = input ("Write a number between 0 and 9: ")
    number_from_user = int (input_from_user)
    return number_from_user

def verify_number ():
    input_from_user = read_number ()
    number_from_user = int (input_from_user)
    while number_from_user not in range (0,10):
        new_number = input ("Write another number: ")
        number_from_user = int (new_number)
        if number_from_user in range (0,10):
            return number_from_user
            break
    else:
        return number_from_user
            
final_number = verify_number ()
print (final_number)

#### Sonjas code ends here ####

#play_guess_the_number(secret_number)

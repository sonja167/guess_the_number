from random import randint
max_number = 99
secret_number = randint(0, max_number)

#### Sonjas code starts here #####


def read_number(text_for_user):
    input_from_user = input(text_for_user)
    number_from_user = int(input_from_user)
    return number_from_user


def read_until_smaller_or_equal_than_max(max_number):
    # the user writes a number
    number_from_user = read_number("Write a number between 0 and "+str(max_number)+": ")
    # while the number is NOT between 0 and max number...
    while number_from_user not in range(0, max_number+1):
        # ... the user writes a new number
        number_from_user = read_number("Write another number: ")
    # return the number (which we know is between 0 and max)
    return number_from_user


def play_guess_the_number(secret_number, max_number):
    number_between_0_and_max = read_until_smaller_or_equal_than_max(max_number)
    if number_between_0_and_max == secret_number:
        print("you WON!!!!!!!!")
    else:
        print("you LOSE :_( the secret number was "+str(secret_number))

#### Sonjas code ends here ####


play_guess_the_number(secret_number, max_number)


# THINGS TO IMPROVE
# 1. characters break the game (needs error handling)
# 2. you can only guess once :(

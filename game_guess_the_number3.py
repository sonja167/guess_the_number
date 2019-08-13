from random import randint
max_number = 5
secret_number = randint(0, max_number)


def read_number(text_for_user):
    input_from_user = input(text_for_user)
    number_from_user = int(input_from_user)
    return number_from_user


def read_until_smaller_or_equal_than_max(max_number):
    number_from_user = read_number("Write a number between 0 and "+str(max_number)+": ")
    while number_from_user not in range(0, max_number+1):
        number_from_user = read_number("You're number is not in the required range. Write another number: ")
    return number_from_user


def play_guess_the_number (secret_number):
    number_between_0_and_max = read_until_smaller_or_equal_than_max (max_number)
    while number_between_0_and_max != secret_number:
        print ("You guessed wrong. Try again!")
        number_between_0_and_max = read_until_smaller_or_equal_than_max (max_number)    
    print ("YOU WON, CONGRATULATIONS! The secret number was " + str(secret_number))


play_guess_the_number (secret_number)




# THINGS TO IMPROVE
# 1. characters break the game (needs error handling)
# 2. you can only guess once :(

# Magic number game

# Prompt the user for input
# Generate a random number using a python library (should be between 1-10)

# check that the number against the magic number
# Let the user know if he/she has won or
    # If the guess was above or under


import random
import time
random_number = random.randint(0, 10)
print('Welcome to the magic number game!')
time.sleep(1)
def prompt():
    user_number = int
    while random_number != user_number:
        user_number = int(input('Pick a random number between 0-10: '))
        if user_number == random_number:
            print('You have picked the lucky number! You won!')
        elif user_number < random_number:
            print('Unfortunately you have not won. Your number was below the lucky number')
            #print(input('Try again! Pick another number:'))
        else:
            print('Unfortunately you have not won. Your number was above the lucky number')
            #print(input('Try again! Pick another number:'))
prompt()

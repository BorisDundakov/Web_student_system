#nothing to do with the app

from random import randrange

# stupid program for testing purposes

# Random number between 1 and 10

# If it is less than 5 -- build fails

# If it is 5 or more -- build suceeds

 

def random_number():

    number = randrange(10)

    print(number)

    return number

 

random_number()

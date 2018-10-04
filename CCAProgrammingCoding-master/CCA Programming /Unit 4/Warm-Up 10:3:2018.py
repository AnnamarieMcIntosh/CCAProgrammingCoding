# Warm Up, if/else -  10/3/2018
# Annamarie McIntosh

import random
number = random.randint(1, 5)

guess = int(input("Enter an integer between 1 and 5: "))
if guess == number:
    print("You guessed it!")
else:
    print("Nope.")

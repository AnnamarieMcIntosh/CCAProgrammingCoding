# Unit 3 Lab - Functions & Conditional Control Flow
# Annamarie McIntosh

def num_kind(x):
    '''prints whether a number is positive, negative, or 0'''
    if x > 0:
        print("Your number %s is positive." % (x))
    elif x == 0:
        print("Your number %s is zero." % (x))
    else:
        print("Your number %s is negative." % (x))

def is_vowel(char):
    '''takes a character and returns True if a vowel and returns False otherwise'''
    vowel = ["a", "e", "i", "o", "u"]
    return char.lower() in vowel

def max_of_three(x, y, z):
    '''takes three numbers and returns the largest one'''
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    elif z > x and z > y:
        return z

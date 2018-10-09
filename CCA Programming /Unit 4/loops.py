# Unit 4 Lab - Getting a Little Loopy
# Annamarie McIntosh

def loops():
    """ Prints digits 0 through 9 on the same twice"""
    x = 0
    for n in range(0, 10):
        print(n, end=" ")
    print("")
    while x < 10:
        print(x, end=" ")
        x += 1

def reverse_string(string):
    """takes a string as an argument and returns the characters in the string reversed."""
    x = ""
    for char in string:
        x = char + x
    print(x)


def max_in_list(l):
    '''takes a list of positive, non-zero, integers and returns the largest integer in the list.'''
    x = 0 
    for n in l:
        if x < n:
            x = n
    print(x)

def yes_or_no(prompt):
    '''Takes a question as an input and prompts user to answer with "yes" or "no"'''
    while True:
        answer = input(prompt + " ").lower()
        if answer == "yes" or answer == "y":
            return True
        elif answer == "no" or answer == "n":
            return False
        else:
            print("Please give a yes or no answer.")
        
def yes_or_no2(prompt):
    '''Takes a question as an input and prompts user to answer with "yes" or "no"'''
    done = False
    while not done:
        answer = input(prompt + " ").lower()
        if answer == "yes" or answer == "y":
            result = True
            done = True
        elif answer == "no" or answer == "n":
            result = False
            done = True
        else:
            print("Please give a yes or no answer.")
    return result

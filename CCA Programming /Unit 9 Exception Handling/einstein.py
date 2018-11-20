'''
Einstein's Puzzle - Lab 9
Annamarie McIntosh
This module implements 'Einstein's favorite puzzle'.
'''

def yes_or_no(prompt_str):
    """
    Prompts user with given prompt string repeatedly
    until they give a valid yes or no response
    returns True if the user responds yes and False if the user resonds no.
    """
    while True: # repeat until user give valid yes or no response
        answer = input(prompt_str + " ")
        lc_answer = answer.lower()
        if lc_answer in ("yes", "y"):
            return True
        elif answer in ("no", "n"):
            return False


def get_int(question):
    """
    Asks the user to input a number repeatedly using the given prompt
    string until the user enters an integer. If the user does not enter
    an integer, this function should prevent a runtime error by adding an
    exception handler that reminds the user that we are requesting an 
    integer value.
    prompt_str: use this string to prompt the user for an integer.
    Returns an integer.
    """
    while True:
        response = input(question)
        try:
            num = int(response)
        except ValueError:
                print("That's not a number!")
        else:
                return num
            
        

def check_diff(num):
    """
    Make sure that the first and last digit differ by at least 2
    num: given number to check
    returns True if first and last digit of num differ by at least 2,
            otherwise returns False
    """
    nums = str(num)
    digit1 = int(nums[0])
    digit2 = int(nums[-1])
    return abs(digit1 - digit2) >= 2


def get_digits():
    """
    Ask for a 3 digit number repeatedly by calling get_num() passing
    the varible, question, as the prompt string.  Continue calling get_num()
    util we get a positive integer that is exactly three digits long and whose
    first and last digit differ by at least two(use check_diff() to test this)
    Returns the first number that meets these criteria
    """
    question = "Enter a 3-digit number whose 1st and last digit differ by at least 2:"
    while True: # repeat until we get a good number
        num = get_int(question)
        diff_ok = check_diff(num)
        if num not in range(100, 1000):
            print ("The number must be three digits.")
        elif not diff_ok:
            print ("The first and last digit must differ by at least 2.")
        else:
            return num


def reverse_number(n):
    """
    Returns the reverse of a given number, n. I.e. if given 123, returns 321.
    """
    x = ""
    str_n = str(n)
    for char in str_n:
        x = char + x
    return int(x)


def einstein_puzzle(n):
    """
    This function implements Einstein's favorite puzzle.
    The function is given a three digit number where the first and
    last digit differ by at least two.
    1) first we reverse it
    2) then subtract the smaller from the larger to get a new number
    3) once this is done, reverse the result
    4) add the new number and its reverse together
    The answer should always be 1089.
    Given a valid number, n, perform the above einstein puzzle calculations
    and return the result.
    """
    step1 = reverse_number(n)
    step2 = abs(step1 - n)
    step3 = reverse_number(step2)
    step4 = step2 + step3
    return step4


def main():
    repeat = True
    while repeat:
        num = get_digits()
        answer = einstein_puzzle(num)
        print("Answer is", answer)
        print()
        repeat = yes_or_no("Try another?")
        print()


if __name__ == "__main__":
    main()


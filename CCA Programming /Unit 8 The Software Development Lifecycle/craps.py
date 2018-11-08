# Lab 8 - Craps
# Annamarie Mcintosh

from die import *


def yes_or_no(prompt_str):
    '''
    Prompts the user with given prompt string repeatedly
    until they give a valid yes or no response.
    Returns True if the user responds yes and False if the user responds no.
    '''
    yes_response = ["yes", "y"]
    no_response = ["no", "n"]
    while True:
        response = input(prompt_str + " ").lower()
        if response in yes_response:
            return True
        elif response in no_response:
            return False
        else:
            print("Please give a yes or no answer.")

def roll_dice(die1, die2):
    '''
    Simulates the rolling of two dice.
    Rolls both dice, prints their value, then returns their sum.
    '''
    input('Hit "Return" to roll the dice ')
    die1.roll()
    die2.roll()
    print(die1, die2)
    total_sum = die1.value() + die2.value()
    return total_sum


def craps():
    '''
    Play single game of craps. Returns True if win and False if loss.
    '''
    die1 = Die()
    die2 = Die()
    come_out = roll_dice(die1, die2)
    print("Your comeout roll is %s." % come_out)
    if come_out == 7 or come_out == 11:
        return True
    elif come_out == 2 or come_out == 3 or come_out == 12:
        return False
    else:
        point = come_out
        print("A point has been established at %s." % point)
        while True:
            phase_2 = roll_dice(die1, die2)
            print("Your roll is %s. " % phase_2)
            if phase_2 == point:
                return True
            elif phase_2 == 7:
                return False

            
def main():
    repeat = True
    while repeat:
        print("Hello! Welcome to Craps!")
        if craps():
            print("You win!")
        else:
            print("You lose.")
        print()
        repeat = yes_or_no("Play again?")
        print()

if __name__ == "__main__":
    main()
      



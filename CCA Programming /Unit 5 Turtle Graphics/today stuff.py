def countdown(num):
    if num > 0 :
        print(num)
        countdown(num-1)
    else:
        print("Done")

def yes_or_no(prompt):
    '''Takes a question as an input and prompts user to answer with "yes" or "no"'''
    yes_answer = ["yes", "y", "yep"]
    no_answer = ["no", "n", "nope"]
    while True:
        answer = input(prompt + " ").lower()
        if answer in yes_answer:
            return True
        elif answer in no_answer:
            return False
        else:
            print("Please give a yes or no answer.")


def yes_or_no2(prompt):
    '''Takes a question as an input and prompts user to answer with "yes" or "no"'''
    yes_answer = ["yes", "y", "yep"]
    no_answer = ["no", "n", "nope"]
    
    answer = input(prompt + " ").lower()
    if answer in yes_answer:
        return True
    elif answer in no_answer:
        return False
    else:
        print("Please give a yes or no answer.")
        return yes_or_no2(prompt)

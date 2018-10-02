# Functions and Conditionals Lab Bonus
# Annamarie McIntosh

import random

def intro():
    print("Hello! Welcome to the chatbot.")
def greeting():
    print("Let's have a deep conversation about my favorite topic.")
def dating():
    print("I have been looking for a partner. I am 105 years old.")
    print("During the day, I am a ceral killer. At night, I am Batman.")
    rep = input("Soooo, come here often?")
    if rep == "yes":
        print("Sorry, you took long, I have a significant other.")
    elif rep == "no":
        print("That's good because I lost interest.")
    else:
        print ("Please respond with either yes or no.")
def art():
    rep = input("Do you want to see a piece of artwork?")
    if rep == "yes" or rep == "yah":
        random_art = random.choice(ascii_art)
        print(random_art)
def is_valid_input(response, all_valid_inputs):
    if response in all_valid_inputs:
        return True
    else:
        return False

greeting_promt = ["hi", "hello", "howdy"]
dating_prompt = ["Hello;)", "love me", "I've been looking for a partner", "I need a partner in crime"]
art_prompt = ["I like art", "show me art", "Show me art", "art", "Art"]
exit_prompt = ["bye", "goodbye", "exit", "Exit"]

def main():
    valid_input = ["hi", "hello", "howdy", "Hi!", "Hello;)", "love me", "I've been looking for a partner", "I need a partner in crime", "I like art", "show me art", "Show me art", "art", "Art", "bye", "goodbye", "exit", "Exit"]
    intro()
    while True:
        answer = input("(What will you say?) ")
        if is_valid_input(answer, valid_input):
            if answer in greeting_promt:
                greeting()
            elif answer in dating_prompt:
                dating()
            elif answer in art_prompt:
                art()
            elif answer in exit_prompt:
                print("Goodbye! I will miss you.Come back again soon!")
                break
        else:
            print("These are the inputs I understand:")
            for vi in valid_input:
                print (vi)
            print("... I don't understand anything else.")



main()

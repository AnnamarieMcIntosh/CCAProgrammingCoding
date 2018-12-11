'''
Hangman - Final Lab
Annamarie McIntosh

This module implements the game, hangman.
'''
import random

HANGMAN_PICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']



def yes_or_no(prompt_str):
    '''
    Prompts user with given prompt string repeatedly
    until they give a valid yes or no response
    returns True if the user responds yes and False if the user resonds no.
    '''
    while True: # repeat until user give valid yes or no response
        answer = input(prompt_str + " ")
        lc_answer = answer.lower()
        if answer in ('y', 'yes'):
            return True
        elif answer in ('n', 'no'):
            return False


def display_board(missed, word_status):
    '''
    missed - a list of all missed letters guessed so far.
    word_status - list with underscores and letters, showing the guessed word so far 
    This function displays the current state of the game board.
    This includes the current state of the hangman using HANGMANPICS,
    The list of missed letters,
    and the current word status with letters appearing for correct guesses
    and the '_' character for unguessed letters.
    Spaces should separate the list of guessed letters as well as the letters
    '_' characters of the word status.
    
    i.e.
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========

    Missed letters: i e u 
    o _ _ _ a _ 
    '''
    print(HANGMAN_PICS[len(missed)])
    print("Missed letters: %s" % " ".join(missed))
    print(" ".join(word_status))
    
    



def get_guess(already_guessed):
    '''
    Takes a list of the characters that the user has already guessed.
    This function repeatedly asks the player to enter a letter until they
    respond with a single letter that has not already been guessed.
    The user should be told if they failed to enter a single alphabetic
    character or if the letter has already been guessed. 
    '''
    while True:
        guess = input("Enter a leter: ")
        if guess.isdigit() == True:
            print("This is not a letter. Please type a LETTER.")
        elif guess in already_guessed:
            print("This letter has already been guessed. Please choose a different letter.")

        elif len(guess) > 1:
            print("Please type only ONE letter.")
        else:
            return guess


def hangman(word):
    '''
    This function implements a single game of hangman.  Given a secret word the user is
    repeatedly asked to guess a letter in that word. The user is allowed six incorrect guesses.
    '''
    print('H A N G M A N')
    missed = []
    correct = []
    word_status = ["_"]*len(word)

    game_over = False
    max_wrong = len(HANGMAN_PICS) - 1

    while not game_over:
        display_board(missed, word_status)
        print()
        # get the next guess
        guess = get_guess(missed + correct)
        if word == guess:
            
        # check if the guessed letter is in the mystery word
        #    if so, did the user guess all the letters?
        #       if so, print the final board and tell the user that they guessed correctly.
        # otherwise check if user is out of guesses
        #    if so, print the final board and tell the user that they ran out of guesses.

    # dont forget to return True or False


def main():
    '''
    Reads an external file to initialize the list of hangman words to choose from.
    Repeatedly selects a word from the list and initiates a game of hangman until the
    user says that he or she wants to stop.
    '''
    wordfile = open("wordlist.txt", "r")
    word_list = wordfile.readlines()
    
    repeat = True
    while repeat:
        word = word = random.choice(word_list)[:-1]
        if hangman(word):
            print("You win!")
        else:
            print("You lose.")
        print()
        repeat = yes_or_no("Play again?")
        print()
    print("Goodbye.")


if __name__ == "__main__":
    main()

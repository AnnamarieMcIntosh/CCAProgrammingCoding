'''
File Input/Output - Lab 11 - Part II
<Your name(s) go here!!!!>

This module implements a couple of instructional file input/output functions.
'''


def open_file(prompt):
    '''
    This helper function will prompt the user for a filename to open, open
    the file and return the open file object.  If the file cannot be found,
    it will handle any exceptions and allow the user to enter another filename
    until a file is successfully opened.
    '''
    pass


def print_upper_file():
    '''
    This function opens an input file, reads it one line at a time, converts
    each line to all uppercase, then prints it to the screen.
    It then prints the number of lines processed.
    See the example in your lab description.
    '''
    file = open_file("Print which file in upper case? ")

    
        
def create_usernames():
    '''
    This function opens a file containing a list of first and last names
    and creates a new file of corresponding account usernames where each
    username is made up of the first character of the first name and the
    first 7 characters of the last name.  Usernames should be in all lower
    case.  See the example in your lab description.
    Open the file "names.txt"
    Write your user names to the file "account_names.txt"
    '''
    pass
        

def main():
   print_upper_file()
   create_usernames()
            
    
if __name__ == "__main__":
    main()

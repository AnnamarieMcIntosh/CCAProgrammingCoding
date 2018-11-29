'''
File Input/Output - Lab 11 - Part II
Annamarie McIntosh

This module implements a couple of instructional file input/output functions.
'''


def open_file(prompt):
    '''
    This helper function will prompt the user for a filename to open, open
    the file and return the open file object.  If the file cannot be found,
    it will handle any exceptions and allow the user to enter another filename
    until a file is successfully opened.
    '''
    while True:
        file_name = input(prompt)
        try:
            in_file = open(file_name, "r")
        except FileNotFoundError:
            print("That file cannot be found. Please try again.")
        else:
            return in_file


def print_upper_file():
    '''
    This function opens an input file, reads it one line at a time, converts
    each line to all uppercase, then prints it to the screen.
    It then prints the number of lines processed.
    See the example in your lab description.
    '''
    file = open_file("Print which file in upper case? ")
    line_count = 0
    for line in file:
        print(line.upper(), end = "" )
        line_count += 1
    print("%s lines processed." % (line_count))
    file.close()
    
        
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
    names_file = open_file("Input names file: ")
    usernames_file = open_file_write("Output Usernames file: ") # Wrote extra function, check bottom
    for line in names_file:
        split_names = line.split()
        first_name = split_names[0]
        last_name = split_names[1]
        fletter = first_name[0]
        letters7 = last_name[:7]
        done_user = fletter + letters7
        usernames_file.write(done_user.lower() + "\n")
    print("Usernames have been written to account_names.txt")
    

def main():
##   print_upper_file()
##   create_usernames()
    pass      
    
if __name__ == "__main__":
    main()

## FOR EASIER USE TO OPEN WRITING

def open_file_write(prompt):
    '''
    This helper function will prompt the user for a filename to open, open
    the file and return the open file object.  If the file cannot be found,
    it will handle any exceptions and allow the user to enter another filename
    until a file is successfully opened.
    '''
    while True:
        file_name = input(prompt)
        try:
            out_file = open(file_name, "w")
        except FileNotFoundError:
            print("That file cannot be found. Please try again.")
        else:
            return out_file

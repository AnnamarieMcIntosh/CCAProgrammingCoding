'''
Demonstration file read functions
'''
def do_read():
    '''
    The read() function returns the entire remaining contents of the
    file as a single (possibly large, multi-line) string.
    '''
    infile = open("poe.txt",'r')
    data = infile.read()
    print(data)
    infile.close()

def do_readlines():
    '''
    The readlines() function returns a list of the remaining lines in the file.
    Each list item is a single line including the newline characters.
    '''
    infile = open("poe.txt",'r')
    lines = infile.readlines()
    print(lines)
    infile.close()
    
def do_readline():
    '''
    The readline() function returns the next line of the file.
    This is all text up to and including the next newline character.
    This example shows the use of readline() within a while loop.
    line becomes False when it reaches EOF (End of File).
    '''
    infile = open("poe.txt",'r')
    line = infile.readline()
    while line:
        print(line, end = "")
        line = infile.readline()
    infile.close()
    
def do_for():
    '''
    An open file can be used as a for loop sequence.  Each iteration
    returns the next line in the file, up to and including the newline character.
    '''
    infile = open("poe.txt",'r')
    for line in infile:
        print(line, end = "")
    infile.close()
    
def main():
    do_read()
    do_readlines()
    do_readline()
    do_for()

#main()

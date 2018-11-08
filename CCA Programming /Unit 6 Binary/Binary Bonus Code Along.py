def bin2num(bin_str):
    '''
    Takes a binary string (a string containing only 1's and 0's)
    and returns the equivalent base 10 number
    '''
    rev_str = bin_str[::-1]
    s = 0
    place = 0
    for c in rev_str:
        digit = int(c)
        s = s + digit * (2**place)
        place += 1
    return s
    

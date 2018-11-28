'''
Strings - Lab 10 - Part I
<Annamarie McIntosh>

This module defines two functions that allow you to replace a character
within a string using two different implementations.  The first uses string
slicing, and the second uses list string/list conversions.  Be sure to test
your functions on indexes that are out of range.
'''

def replace_char1(a_str, idx, char):
    """
    Given a string, a_str, this function should return a new string where the
    character in the idx position is replaced with the given character, char.
    This implementation should use string slicing to accomplish this task.
    """
    string1 = a_str[:idx]
    string2 = a_str[idx + 1:]
    final = string1 + char + string2
    print final

def replace_char2(a_str, idx, char):
    """
    Given a string, a_str, this function should return a new string where the
    character in the idx position is replaced with the given character, char.
    This implementation should use string/list conversions to accomplish this
    task.
    """
    l = list(a_str)
    l[idx] = char
    final = "".join(l)
    print final


## replace_char1("happy", 1, "o")
replace_char2("happy", 1, "o")

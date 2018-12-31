# String processing utility functions
#

""" Convert all alphabetical characters in a string to uppercase.
"""
def upper_char(x):
    x = list(x)
    for i in range(len(x)):
        x[i] = x[i].upper()
    x = "".join(x)
    return x 

# SETUP
from learntools.core import binder; binder.bind(globals())
from learntools.python.ex2 import *
print('Setup complete.')

def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)
    return round(num,2)
    pass

# Check your answer
q1.check()

def to_smash(total_candies,n_friends=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
  
    return total_candies % n_friends

# Check your answer
q3.check()

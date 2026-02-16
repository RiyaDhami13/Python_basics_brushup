from learntools.core import binder; binder.bind(globals())
from learntools.python.ex4 import *
print('Setup complete.')

def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    if len(L) < 2:
        return None 
    return L[1]
    pass

# Check your answer
q1.check()

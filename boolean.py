#Setup Complete
from learntools.core import binder; binder.bind(globals())
from learntools.python.ex3 import *
print('Setup complete.')

# Your code goes here. Define a function called 'sign'
def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0
# Check your answer
q1.check()

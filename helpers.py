# helpers.py
def display(message, is_warning=False):
    if is_warning:
        print('Warning!!')
    print(message)

# import module as namespace
import helpers 
helpers.display('Not a warning')

#import all into current namespace
from helpers import *
display('Not a warning')

# import specific items into current namespace
from helpers import display
display('Not a warning')
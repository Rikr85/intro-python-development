# # helpers.py
# def display(message, is_warning=False):
#     if is_warning:
#         print('Warning!!')
#     print(message)

# # import module as namespace
# import helpers 
# helpers.display('Not a warning')

# #import all into current namespace
# from helpers import *
# display('Not a warning')

# # import specific items into current namespace
# from helpers import display
# display('Not a warning')

# # Installing packages
# # Install an individual package
# pip install colorama

# # Install from a list of packages
# pip install -r requirements.txt 

# # requirements.txt
# colorama
from pip._vendor.colorama import init, Fore

def display(message, is_warning=False):
    if is_warning:
        print(Fore.RED + message)
    else:
        print(Fore.BLUE + message)

# first_name = 'Christopher'
# last_name = 'Harrison'

# # first_name = input('Please enter your first name: ')
# # last_name = input('Please enter your last name: ')
# # # print(first_name + last_name)
# # print('Hello, ' + first_name + ' ' + last_name.capitalize())

# #Custom string formatting 
# output = 'Hello, ' + first_name + ' ' + last_name
# output = 'Hello, {}{}'.format(first_name, last_name)
# output = 'Hello, {0}{1}'.format(first_name, last_name)
# #Only available in Python 3  
# output = f'Hello, {first_name}{last_name}'
# print(output)
# import helpers
# helpers.display('Sample message test', True)

from helpers import display
display('Sample message', True)
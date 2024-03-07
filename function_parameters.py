# ----------------------------------------------------------
# def get_initial(name):
#     initial = name[0:1].upper()
#     return initial
# first_name = input('Enter your first name: ')
# first_name_initial = get_initial(first_name)

# print('Your initial is: ' + first_name_initial)

# ----------------------------------------------------------
# Functions can accept multiple parameters
def get_initial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name, False)

print('Your initial is: ' + first_name_initial)
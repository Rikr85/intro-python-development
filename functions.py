# --------------------------------------------------------------
# Sometimes we copy and paste our code
# import datetime
# print timestamps to see how long sections of code
# take to run

# first_name = 'Susan'
# print('task completed')
# print(datetime.datetime.now())
# print()

# for x in range(0,10):
#     print(x)
# print('task completed')
# print(datetime.datetime.now())
# print()
# --------------------------------------------------------------
# Using functions instead of repeating code
# import datetime
# # Print the current time
# def print_time():
#     print('task completed')
#     print(datetime.datetime.now())
#     print()

# first_name = 'Susan'
# print_time()

# for x in range(0,10):
#     print(x)
# print_time()
# --------------------------------------------------------------
# Pass the task name as a parameter
from datetime import datetime

# Print the current time and task name
def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()

first_name = 'Susan'
print_time('first name assigned')

for x in range(0,10):
    print(x)
print_time('loop completed')
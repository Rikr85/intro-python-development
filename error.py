# Error handling
# Error types
# - Syntax errors
# - Runtime errors
# - Logic errors

# Syntax errors
# This code won't run at all
# x = 42
# y = 206

# if x == y
#     print('Success!!')

# Runtime errors
# This code will fail when run
# x = 42
# y = 0
# print(x / y)

# Logic errors
x = 206
y = 42
if x < y:
    print(str(x) + ' is greater than ' + str(y))

# Catching runtime errors
# try:
#     print(x / y)
# except ZeroDivisionError as e:
#     # Optionally, log e somewhere
#     print('Sorry, something went wrong')
# except:
#     print('Something really went wrong')
# finally:
#     print('This always runs on success or failure')
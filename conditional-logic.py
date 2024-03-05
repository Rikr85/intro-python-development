# price = input('how much did you pay?')

# price = float(price)
# if price >= 1.00:
#     tax = .07
#     print('Tax rate is: ' + str(tax))


price = input('how much did you pay?')
price = float(price)
if price >= 1.00:
    tax = .07
    print('Tax rate is: ' + str(tax))
else:
    tax = 0
    print('Tax rate is: ' + str(tax))
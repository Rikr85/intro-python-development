# country = input('What country do you live in?')
# province = input('What province/state do you live in?')

# if country == 'Canada':
#     if province in ('Alberta',\
#                     'Nunavut','Yukon'):
#         tax = 0.05
#     elif province == 'Ontario':
#         tax = 0.13
#     else:
#         tax = 0.15
# else:
#     tax = 0.0
# print(tax)

country = input('What country do you live in?')

if country.lower() == 'Canada':
    province = input('What province/state do you live in?')
    if province in ('Alberta',\
                    'Nunavut','Yukon'):
        tax = 0.05
    elif province == 'Ontario':
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0.0
print(tax)
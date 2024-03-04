#To get current date and time 
#we need to use the datetime library

from datetime import datetime
current_date = datetime.now()

#the now function returns a datetime object 

print('Today is: ' + str(current_date))

from datetime import datetime, timedelta
today = datetime.now()
print('Today is: ' + str(today))

#timdelta is used to define a period of time

one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))

from datetime import datetime
current_date = datetime.now()

print('Day: ' + str(current_date.day))
print('Month: ' + str(current_date.month))
print('Year: ' + str(current_date.year))


from datetime import datetime
birthday = input('When is your birthday (dd/mm/yyyy)?')

birthday_date = datetime.strptime(birthday, '%d/%m/%Y')

print('Birthday: ' + str(birthday_date))
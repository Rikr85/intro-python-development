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
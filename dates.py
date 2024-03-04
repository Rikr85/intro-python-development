#To get current date and time 
#we need to use the datetime library
from datetime import datetime

current_date = datetime.now()
#the now function returns a datetime object 
print('Today is: ' + str(current_date))
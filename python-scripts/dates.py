### Dates ###

#First we need to import the library
import datetime

now = datetime.datetime.now() #This is the way to access the datetime 'now'
print(now)

timestamp = now.timestamp()

print(timestamp) #a timestamp is a sequence of characters identifying when a certain event took place
#A timestamp is helful when working with dates because it's easier to transmit 

#We can also create an instance of a datetime object
year_2023 = datetime.datetime(2023, 9, 16)
print(year_2023)
print(year_2023.timestamp())

from datetime import time

current_time = time() #Initially, time is an empty object (it's attributes are)
print(current_time)

current_time_filled = time(20, 7, 39)
print(current_time_filled)

from datetime import date

current_date = date(2023, 5, 23)
#current_date = date() If we try to print this instance attributes it will throw an exception
#An instance can be re-initialized
current_date = date(current_date.year, current_date.month, current_date.day+1)

print(current_date.year)
print(current_date.month)
print(current_date.day)

diff = now.date() - current_date
print(diff)

from datetime import timedelta #Timedelta allows operations between dates or times

start_timedelta = timedelta(300, 10, 300, weeks = 7)
end_timedelta   = timedelta(400, 100, 100, weeks = 13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
print(end_timedelta / start_timedelta)

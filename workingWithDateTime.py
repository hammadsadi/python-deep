import datetime

# Current date and time
current_date_time = datetime.datetime.now()
# print(current_date_time)

#  Year
# print(current_date_time.year)
# Month
# print(current_date_time.month)

# Day
# print(current_date_time.day)

#  Date
# print(current_date_time.date())

#  Time
# print(current_date_time.time())

#  Weekday
# print(current_date_time.weekday())

#  Minute
# print(current_date_time.minute)

# Second
# print(current_date_time.second)

#  Microsecond
# print(current_date_time.microsecond)


#  Format date and time
formated_date = current_date_time.strftime('%d/%m/%y')
formated_time_second = current_date_time.strftime('%H:%M:%S')
# print(formated_time_second)


#   Date Time Difference

date1 = datetime.datetime(2020, 5, 1)
date2 = datetime.datetime(2023, 5, 1)
difference = date2 - date1
# print(difference)

#  Add Extra Time
# date1 += datetime.timedelta(days=9)
# print(date1)


#  Minus Extra Time
date1 -= datetime.timedelta(days=1)
print(date1)
























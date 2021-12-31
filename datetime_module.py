import datetime as dt

#date
current_date = dt.date.today()

print(current_date)
print("Year:", current_date.year)
print("Month:", current_date.month)
print("Day:", current_date.day)


#time
time1 = dt.time(10, 45, 30, 45667)

print(time1)


#datetime
datetime_obj = dt.datetime(2021, 11, 28, 23, 55, 59)

print(datetime_obj)
print(datetime_obj.date())
print(datetime_obj.time())


#strptime() - converts string to daytime objects
date_string = "01 January, 2022"
date_object = dt.datetime.strptime(date_string, "%d %B, %Y")

print("Date object:", date_object)


#strftime() - converts daytime objects to strings
present_datetime = dt.datetime.now()
string_date = present_datetime.strftime("%A, %B %d, %Y")
diff_format = present_datetime.strftime("%b %-d, %I%p")

print(string_date)
print(diff_format)

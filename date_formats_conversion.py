# convert UK date to US date
# UK date(string)
#       |strptime()
# datetime object
#       |strftime()
# US date(string)


import datetime as dt

UK_date = dt.datetime(2021, 11, 1)
datetime_obj = UK_date.strftime("%d,%B,%Y")
print(datetime_obj)
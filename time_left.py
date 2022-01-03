#create a program to that tells us how many days, months, years left in our life

age = input("Enter your age? ")

age_as_int = int(age)

days_left = (100 - age_as_int) * 365
weeks_left = (100 - age_as_int) * 52
months_left = (100 - age_as_int) * 12

print(days_left)
print(weeks_left)
print(months_left)
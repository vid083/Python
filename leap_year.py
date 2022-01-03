

year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f" {year} is a leap year")
        else:
            print(f" {year} is not a leap year")
    else:
       print(f" {year} is a leap year") 
else:
    print(f" {year} is not a leap year")



# 2000/4 = 5 (leap)
# 2000/100 = 20 (not leap)
# 2000/400 = 5 (leap)
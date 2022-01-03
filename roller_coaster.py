
print("welcome to roller coaster!")

height = int(input("Enter your height in cms: "))

bill = 0
if height >= 120:
    print("you can ride")
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 5
        print("children ticket is $5")
    elif age <= 18:
        bill = 7
        print("youth ticket is $7")
    else:
        bill = 15
        print("adult ticket is $15")

    wants_photo = input("do you want a photo? Y or N ")
    if wants_photo == "Y":
        bill += 3
    print(f"Final bill is {bill}")
else:
    print("you can't ride")



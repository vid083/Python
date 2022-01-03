
print("Welcome to frienship calculator!")

name1 = input("Enter your name: \n")
name2 = input("Enter your friend name: \n")

Name1 = name1.lower()
Name2 = name2.lower()
Name = Name1 + Name2

t = Name.count("t")
r = Name.count("r")
u = Name.count("u")
e = Name.count("e")

true = t+r+u+e

f = Name.count("f")
r = Name.count("r")
n = Name.count("n")
d = Name.count("d")

frnd = f+r+n+d

frndshp_score = int(str(true) + str(frnd))

if (frndshp_score < 10) or (frndshp_score > 90):
    print(f"Your score is {frndshp_score}, you are like coke and mentos")
elif (frndshp_score >= 40) and (frndshp_score <= 50):
    print(f"Your score is {frndshp_score}, you are alright together")
else:
    print(f"Your score is {frndshp_score}")

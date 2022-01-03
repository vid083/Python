
height = float(input("Enter your height: "))
weight = int(input("Enter your weight: "))

BMI = round(weight / height**2)
if BMI < 18.5:
    print(f"your BMI is {BMI} and you are underweight")
elif BMI < 25:
    print(f"your BMI is {BMI} and you are normal weight")
elif BMI < 30:
    print(f"your BMI is {BMI} and you are over weight")
elif BMI < 35:
    print(f"your BMI is {BMI} and you are obese")
else:
    print(f"your BMI is {BMI} and you are clinical obese")




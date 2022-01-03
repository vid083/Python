

print("welcome to tip calculator")
bill = float(input("what was the total bill? $"))
tip = int(input("what percentage tip would you like to give?, 10 or 12 or 15? "))
num_people = int(input("how many people to split the bill? "))

split_bill = ((tip/100 * bill + bill) / num_people)
final_bill = "{:.2f}".format(split_bill)
#final_bill = round(split_bill,2)

print(f"Each person should pay : , {final_bill}")

#input:
# 124.56
# 12
# 7

# logic: (124.56 * 1.12)/7

# output : 19.93
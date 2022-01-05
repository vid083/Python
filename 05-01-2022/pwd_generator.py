import random
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
lower_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
  
upper_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
  
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
           '*', '(', ')', '<']

print("Welcome to the Python Password Generator!")
num_upp_letters = int(input("How many uppercase letters? \n"))
num_low_letters = int(input("How many lowercase letters? \n"))
num_symbols = int(input("How many symbols? \n"))
num_numbers = int(input("How many numbers? \n"))

password = []
for i in range(1,num_upp_letters+1):
    password.append(random.choice(upper_char))

for i in range(1,num_low_letters+1):
    password.append(random.choice(lower_char))

for i in range(1,num_symbols+1):
    password.append(random.choice(symbols))

for i in range(1,num_numbers+1):
    password.append(random.choice(numbers))
print(password)
random.shuffle(password)
print(password)

pwd = " "
for each_char in password:
    pwd += each_char

print(pwd)
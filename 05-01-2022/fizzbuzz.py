# if number divisible by 3 then print Fizz
# if number divisible by 5 then print Buzz
# if number divisible by 3 and 5 then print FizzBuzz

for numbers in range(1, 15):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print("FizzBuzz")
    elif numbers % 3 == 0:
        print("Fizz")
    elif numbers % 5 == 0:
        print("Buzz")
    else:
        print(numbers)



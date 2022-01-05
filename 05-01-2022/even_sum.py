# sum of even numbers from 1 to 100

sum = 0

# for even in range(2,101,2):

for even in range(1,101):
    if even % 2 == 0:
        sum += even
print(sum)
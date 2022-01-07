a = [4,5,6,7,8,4,4]

# find the occurance of 4

print(a.count(4))

occurance = 0
for i in range(len(a)):
    if a[i] == 4:
        occurance += 1
print(occurance)
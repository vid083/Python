a = [-1, 2, -3, -4, 5, 6, 7]
# seperate -ve and +ve numbers into separate lists

''''
1. count =0
2. for loop - if cond - (>0 check)
'''

num = 0
positive = []
negative = []
for n in range(len(a)):
    if a[n] > 0:
        positive.append(a[n])
    else:
        negative.append(a[n])
print(positive)
print(negative)

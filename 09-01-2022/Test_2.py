a = [[1,2,3], 
     [4,5,6], 
     [7,8,9]]

# o/p = 1,2,3,6,5,4,7,8,9 - snack pattern
'''
1. 1st for loop - inner arrays
2. 2nd for loop - each element
3. if cond - index = odd
'''

for i in range(len(a)):
    for j in range(len(a[i])):
        if i % 2 == 0:
            n = a[i][j]
        else:
            n = a[i][-j-1]
        print(n)
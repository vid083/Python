a = [[1,2,3], 
     [4,5,6], 
     [7,8,9]]

# print 1,5,9

'''
1. 1st for loop - for inner arrays - i
2. 2nd for loop - for each element - j
3.  a[0][0], a[1][1], a[2][2] - i=j

'''

for i in range(len(a)):
    for j in range(len(a[i])):
        if i == j:
            print(a[i][j])
ip = [[1,2,3],
      [4,5,6],
      [7,8,9],
      [10,11,12],
      [13,14,15]] 
# Get the first element from each nested list in a list o/p = [1, 4, 7, 10, 13]
'''
a[0][0], a[1][0], a[2][0], a[3][0], a[4][0]
i 
'''
op = []
for i in range(len(ip)):
    for j in range(len(ip[i])):
        if i - j == i:
            op.append(ip[i][j])
print(op)
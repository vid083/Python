a = [[1,2,3], 
     [4,5,6], 
     [7,8,9]]


'''
#  op = [[2,3,1],
#        [6,4,5],
#        [8,9,7]]

1. 1st for loop - for inner arrays - i

 a[0][0]   a[0][1]  a[0][2] --> a[0][1]  a[0][2]  a[0][0]
 a[1][0]   a[1][1]  a[1][2]
'''
op = []
for i in range(len(a)):
    
    if i % 2 == 0:
        result = a[i][1:] + a[i][:1]
        op.append(result)
    else:
        result = a[i][2:] + a[i][:2]
        op.append(result)
print(op)     

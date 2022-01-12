a = [1,2,3,4,5,6]

'''
op = [[1,2],[3,4],[5,6]]

1. slicing [:]
2. empty list, append slices
'''
op = []
n = 2

for i in range(0, len(a), n):
    b = a[i:i + n] 
    op.append(b)
print(op)


'''
i=0; b=a[0:2]
i=2; b=a[2:4]
i=4; b=a[4:6]
'''
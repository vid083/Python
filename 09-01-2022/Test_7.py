a = [1,2,3,4,5,6]

'''
op = [[1,2,3], [4,5,6]]
op = [[1,2],[3,4],[5,6]]

1. slicing [:]
2. empty list, append slices
'''
op = []
b = a[:len(a)//2]
c = a[len(a)//2:]
op.append(b)
op.append(c)
print(op)
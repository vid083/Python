


# reverse of given list
ip = [1,2,3,4,5]

'''
1. for loop

'''
op = []
for i in range(len(ip)):
    
    print(ip[-i-1])
    op.append(ip[-i-1])
print(op)

'''
iterations:

i=0, ip[-0-1]=ip[-1]= 5
i=1, ip[-1-1]=ip[-2]= 4
i=2, ip[-2-1]=ip[-3]= 3
i=3, ip[-3-1]=ip[-4]= 2
i=4, ip[-4-1]=ip[-5]= 1

'''

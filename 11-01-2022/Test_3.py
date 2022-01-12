ip = [1,2,3,4,5,6] 
# make two right shifts, op=[5,6,1,2,3,4]

'''
slicing [:4] + [4:]
'''

a = ip[:4]

op = ip[4:]


op.extend(a)
print(op)
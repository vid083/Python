ip=[121,122,12321,133,154]
"""
op=['p','n','p','n','n']

"""
op = []
for i in range(len(ip)):
    ip[i] = int(ip[i])
    temp = ip[i]
    rev = 0
    while (ip[i]>0):
        #last digit
        num = ip[i] % 10
        # built rev num
        rev = rev * 10 + num
        # remaing num
        ip[i] = ip[i] // 10
    
    if temp == rev:
        # print ("p")
        op.append("p")
    else:
        # print("n")
        op.append("n")
print(op)

'''
each iterations
1st iteration: 121>0
num = 121 % 10 = 1
rev = 0 * 10 + 1 = 1
ip = 121 // 10 = 12

2nd iteration: 12>0
num = 12 % 10 = 2
rev = 1 * 10 + 2 = 12
ip = 12 // 10 = 1

3rd iteration: 1>0
num = 1 % 10 = 1
rev = 12 * 10 + 1 = 121
ip = 1 // 10 = 0

4th iteration: 0>0 --> false
'''

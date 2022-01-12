


ip = [1,2,3,4,5,6]
index = [1,5]   # swaping index
# op = [1,6,3,4,5,2]

''''
1. add first index element to temp variable
2. 5th index element add to 1st index
3. add temp to 5th
'''

op = []
temp = ip[index[0]]
print(ip)
ip[index[0]] = ip[index[1]]
print(temp)
print(ip)
ip[index[1]] = temp
print(ip)

op = ip
print(op)

''''
iterations: 
temp = 2, 

'''

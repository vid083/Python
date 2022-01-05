


ip = [1,2,3,4,5,6,6]
#find the duplicate in above string

''''
1. take the one index element and compare with rest of the string
2. if the element exist in the list, save the element to the op list

'''

op = []
for i in range(len(ip)):
    for j in range(len(ip)):

        # print(f"i = {i}")
        # print(f"j = {j}")
        if ip[i] == ip[j] and i != j:   
            op.append(ip[i]) 
print(op)
            
''''
iterations: 
'''
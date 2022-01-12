ip = [10,1,9,2,8,3,7,10,4,6,5] 
# sort given list and find second-largest number

# b = set(ip)
# print(b)
# c = max(b)
# print(c)


largest = ip[1]
sec_largest = ip[1]

for i in range(len(ip)):
    if ip[i] > largest:
        largest = ip[i]

print(largest)

for i in range(len(ip)):
    if ip[i] > sec_largest and ip[i] != largest:
        sec_largest = ip[i]

print(sec_largest)
    

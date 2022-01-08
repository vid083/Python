a = [1,2,3,4,5,5]

# find the second largest num --> assignment

'''
1. list sort 
2. index = [-2]

a.sort()
b = set(a)
print(b)
'''

largest = a[0]
sec_largest = a[0]
for i in range(len(a)):
    if a[i] > largest:
        largest = a[i]

for i in range(len(a)):
    if a[i] > sec_largest and a[i] != largest:
        sec_largest = a[i]

print(sec_largest)

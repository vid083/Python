a = []
'''
1. add 2 to a
2. append [2,3] to a
3. delete 5th index
4. reverse the list
5. append list a to a
6. sort the list a
7. swap the first and last indices
8. sort in desending order
9. find the index of 1, 2, 3
10. find len, slice half, 3 parts --> assignment

'''
# 1
a.append(2)
print("ouput of 1st q :", a)

b = [2,3]
a.extend(b)
print("ouput of 2nd q :", a)

# a.pop(a[4])
print("ouput of 3rd q :", a)

a.reverse()
print("ouput of 4th q :", a)

a.extend(a)
print("ouput of 5th q :", a)

a.sort()
print("ouput of 6th q :", a)

temp = a[len(a)-1]
a[len(a)-1] = a[0]
a[0] = temp
print("ouput of 7th q :", a) 

a.sort(reverse=True)
print("ouput of 8th q :", a) 

# first = a.index(1)
# print(first)
second = a.index(2)
print(second)
third = a.index(3)
print(third)

print(len(a))


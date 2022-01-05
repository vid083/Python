


# search the given number 'a' in the list 
ip=[1,2,3,4,5,6]
a=6

'''
op: y
index

1. for loop
2. 
'''
index_value = 0
for i in range(len(ip)):

    if ip[i] == a:
        res = "yes"
        index_value = i
        break
    
print(res)
print(index_value)


'''
iterations:

i=0, check ip[0] == a 
            1 != 6

i=1, check ip[1] == a
            2 != 6

i=2, check ip[2] == a
            3 != 6
        
i=3, check ip[3] == a
            4 != 6

i=4, check ip[4] == a
            5 != 6
        
i=5, check ip[5] == a
            6 == 6 (true)(prints "yes")
'''
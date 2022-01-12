
ip = [3,4,5,6,8,10,12,13,14,15,]
"""
3_ip = [3,6,12,15]
4_ip = [4,8,12]
5_ip = [10,15]
ip_34 = [12]
ip_35
ip_45
remaining
-----

1. for loop
2. create empty lists
3. if conditions for multiples
4. append separately 

elif 3& 4
"""
op_3 = []
op_4 = []
op_5 = []
rem = []
op_3_4 = []
op_4_5 = []
op_3_5 = []

for i in range(len(ip)):
    if ip[i] % 3 == 0 and ip[i] % 4 == 0:
        if ip[i] % 3 == 0:
            if ip[i] % 4 == 0:
                op_4.append(ip[i])
                op_3_4.append(ip[i])
            op_3.append(ip[i])

    elif ip[i] % 4 == 0 and ip[i] % 5 == 0:
        
        # print(ip[i])
        op_4.append(ip[i])
    elif ip[i] % 5 == 0:
        # print(ip[i])
        op_5.append(ip[i])
    elif ip[i] % 3== 0 and ip[i] % 4 == 0:
        op_3_4.append(ip[i])
    elif ip[i] % 4== 0 and ip[i] % 5 == 0:
        op_4_5.append(ip[i])
    elif ip[i] % 3== 0 and ip[i] % 5 == 0:
        op_3_5.append(ip[i])
    else:
        # print(ip[i])
        rem.append(ip[i])
print(op_3)
print(op_4)
print(op_5)
print(op_3_4)
print(op_3_5)
print(op_4_5)
print(rem)
    
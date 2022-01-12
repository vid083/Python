
'''
100 
base 2 to base 10

(1*2ˆ2) + (0* 2ˆ1) + (0*2ˆ0)


100
base 17 to base 10

(1* 17ˆ2) + (0*17ˆ1) + (0*17ˆ0)

1A
(1* 17ˆ1) + (10* 17ˆ0) = 17 + 10 = 27

23GF
(2* 17ˆ3) + (3* 17ˆ2) + (G* 17ˆ1) + (F* 17ˆ0) =  (2*4913) + (3*289) + (16*17) + (15*1) = 9826 + 867 + 272 + 15 = 10,980


'''

def conversion(num, base):
    # print(num, base)
    # print(len(num))
    res = 0
    for i in range(len(num)):
        
        p = pow(base,(len(num)-i-1))
        res += (int(num[i]) * p)
    print(res)
        


conversion("1A", 17)

'''
i=0 ; res = 1*(2ˆ(2)) = 4
'''
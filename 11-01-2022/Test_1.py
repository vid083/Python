'''
print given list for n=5 input

* * * * *
* * * *
* * *
* *
* 



'''

def pattern(n):
    for i in range(0,n+1):
        i = '* ' * (n-i)
        # for j in range(1,n):
        #     j = '*'
        print(i)
                

pattern(5)



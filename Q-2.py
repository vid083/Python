def num_pattern(n):
    
    for i in range(0,n):
        num=1
        for j in range(0,i+1):
            print(num , end=" ")
            num=num+1
        print("\r")

n = int(input("Enter n value: "))
num_pattern(n)
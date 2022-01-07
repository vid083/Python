# array of array
a = [[1,2,3], [3,4,5]]

# print(a[0][0])

for i in range(len(a)):
    print(f"i : {i}")
    for j in range(len(a[i])):
        print(f"j : {j}")
        num = a[i][j]

        print(num)
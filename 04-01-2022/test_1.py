
#even or odd
num_list = [2,5,7,8,5,87]
# op=["e","o","o","e","o","o"]

list = []

for i in range(len(num_list)):
    if num_list[i] % 2 == 0:
        # print("e")
        list.append("e")
    else:
        # print("o")
        list.append("o")
print(list)

"""
1. for loop 
2. if cond
3. list append
"""
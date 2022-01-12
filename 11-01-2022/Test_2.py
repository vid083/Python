ip=[2,5,1,4,3] 
# for given input below 
# op={"even_positions_sum":9, 
# "odd_positions_sum":6, 
# even_positions:[5,4], 
# odd_positions:[2,1,3]}

'''
even = 5,4,
odd = 2,1,3
'''
op = {}
even_positions = []
odd_positions = []
odd_positions_sum = 0
even_positions_sum = 0

for p in range(len(ip)):
    if p % 2 == 0:
        term = p // 2
        # print(term)
        res = 2 * (term+1)
        # print(res)
        even_positions.append(res)
        print(f"i {ip[p]}")
        even_positions_sum += res
    
    else:
        res = p
        odd_positions.append(res)
        even_positions_sum += ip[p]

# op[even_positions_sum] = 12
# op[odd_positions_sum] = 9
# op[even_positions]
# op[even_positions]

print(even_positions)
print(odd_positions)
print(even_positions_sum)
print(odd_positions_sum)

op["even_position"] = even_positions
op["odd_position"] = odd_positions
op["even_position_sum"] = even_positions_sum
op["odd_position_sum"] = odd_positions_sum


print(op)
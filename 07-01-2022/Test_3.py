a = [3,4,1,2,3,4,5]

# find the smallest number in the list
# gretest number
#  print the index of small and greast number
#  diff b/w small and greatest

''''
1. counter 
2.loop, if cond check

'''
smallest = a[0]
for i in range(len(a)):
    print(f"this loop for i = {i}")
    if a[i] < smallest:
        print(f"index: {i}, new smallest value= {a[i]}")
        smallest = a[i]
        indexOfSmallest = i
print(smallest)
print(f"index of smallest number: {indexOfSmallest}")


greatest = a[0]
for i in range(len(a)):
    print(f"this loop for i = {i}")
    if a[i] > greatest:
        print(f"index: {i}, new greatest value= {a[i]}")
        greatest = a[i]
        indexOfGreatest = i
print(greatest)
print(f"index of greatest number: {indexOfGreatest}")

diff = greatest - smallest
print(f"diff b/w {diff}")
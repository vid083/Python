def Bubble_sorting(arr):
    
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        
my_arr = list(map(int,input("Enter elements of array: ")))
Bubble_sorting(my_arr)
print(my_arr)



def bubbleSortBasic(arr):
    n = len(arr)  
    for i in range(n-1):  
        for j in range(n - 1):  
            if arr[j] > arr[j + 1]: 
                
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


input_str = input("Enter numbers separated by spaces: ")
arr = list(map(int, input_str.split())) 


sorted_arr = bubbleSortBasic(arr)
print("Sorted Array:", sorted_arr)

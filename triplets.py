def findTriplets(arr, target):
    n = len(arr)  
    triplets = []  
    
    for i in range(n):
        for j in range(i + 1, n):  
            for k in range(j + 1, n):  
                if arr[i] + arr[j] + arr[k] == target:  
                    triplets.append((arr[i], arr[j], arr[k])) 
    return triplets


input_str = input("Enter numbers for the array separated by spaces: ")
arr = list(map(int, input_str.split()))  

target = int(input("Enter the target sum: "))


result = findTriplets(arr, target)
if result:
    print("Triplets with the target sum:", result)
else:
    print("No triplets found with the given target sum.")


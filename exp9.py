def linear_search(arr, target):
    
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  



def binary_search(arr, target):
   
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            left = mid + 1  
        else:
            right = mid - 1  
    
    return -1  


def selection_sort(arr):
    
    n = len(arr)
    
    for i in range(n - 1):
        min_index = i
        
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr



my_list = [4, 2, 7, 10, 9, 5]
target_element = 10
result = linear_search(my_list, target_element)

if result != -1:
    print("Element found at index result",result)
else:
    print("Element  not found.")



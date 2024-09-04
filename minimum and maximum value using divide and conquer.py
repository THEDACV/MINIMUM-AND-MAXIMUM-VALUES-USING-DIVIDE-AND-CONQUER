def find_min_max(arr, low, high):
    
    if low == high:
        return arr[low], arr[low]
    
 
    if high == low + 1:
        return (min(arr[low], arr[high]), max(arr[low], arr[high]))
    
   
    mid = (low + high) // 2
    
    
    min_left, max_left = find_min_max(arr, low, mid)
    
    
    min_right, max_right = find_min_max(arr, mid + 1, high)
    
  
    return min(min_left, min_right), max(max_left, max_right)


if __name__ == "__main__":
    array = [3, 5, 1, 8, 7, 9, 2, 4]
    min_value, max_value = find_min_max(array, 0, len(array) - 1)
    
    print(f"Minimum value: {min_value}")
    print(f"Maximum value: {max_value}")
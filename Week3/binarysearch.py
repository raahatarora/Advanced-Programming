def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_value = sorted_list[mid]
        
        if mid_value == target:
            return mid
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = int(input("Enter the value to search for: "))
    
    result = binary_search(sorted_list, target)
    
    if result != -1:
        print(f"Value {target} found at index {result}.")
    else:
        print(f"Value {target} not found in the list.")

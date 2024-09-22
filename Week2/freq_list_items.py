# To generate a list and find the frequency of each item in the list

def count_frequency(lst):
    frequency = []
    
    for item in lst:
        count = 0
        for i in range(len(lst)):
            if lst[i] == item:
                count += 1
        frequency.append(count)
    
    return frequency

# Example usage
my_list = [1, 2, 3, 2, 1, 3, 4, 1, 2, 3]
result = count_frequency(my_list)

print("List:", my_list)
print("Frequency of each item:", result)

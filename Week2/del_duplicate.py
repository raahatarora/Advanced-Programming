# To create a random list of 15 elements and delete the duplicate elements from that list

import random

def generate_random_list(size, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

def remove_duplicates(input_list):
    return list(set(input_list))


list_size = 15
lower_bound = 1
upper_bound = 100


random_list = generate_random_list(list_size, lower_bound, upper_bound)
print("Original list with possible duplicates:")
print(random_list)


unique_list = remove_duplicates(random_list)
print("\nList after removing duplicates:")
print(unique_list)

def calculate_combinations_sum(tuples_list):
    if not tuples_list:
        return 0

    total_sum = 0
    
    num_combinations = 1
    for t in tuples_list:
        num_combinations *= len(t)
    
    def generate_combinations(tuples_list, current_combination, index):
        nonlocal total_sum
        
        if index == len(tuples_list):
            total_sum += sum(current_combination)
            return
        
        for element in tuples_list[index]:
            generate_combinations(tuples_list, current_combination + [element], index + 1)
    
    generate_combinations(tuples_list, [], 0)
    
    return total_sum

if __name__ == "__main__":
    tuples_list = [(1, 2), (3, 4), (5, 6)]

    result = calculate_combinations_sum(tuples_list)
    print(f"Total sum of all possible combinations: {result}")

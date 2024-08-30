def convert_tuple_to_succeeding_list(tup):
    return [tup[i + 1] if i + 1 < len(tup) else None for i in range(len(tup))]

# Example usage
if __name__ == "__main__":
    tup = (1, 2, 3, 4, 5)
    result = convert_tuple_to_succeeding_list(tup)
    print(result)

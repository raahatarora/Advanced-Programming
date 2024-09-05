def longest_increasing_subsequence(arr):
    n = len(arr)
    lis = [1] * n  # Initialize LIS values for all indexes as 1

    # Compute optimized LIS values in a bottom-up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    # Find the maximum value in lis[]
    maximum = max(lis)

    # Reconstruct the longest increasing subsequence
    lis_sequence = []
    current_length = maximum
    for i in range(n - 1, -1, -1):
        if lis[i] == current_length:
            lis_sequence.append(arr[i])
            current_length -= 1

    lis_sequence.reverse()  # The sequence is constructed in reverse order

    return lis_sequence

# Example usage
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print("Longest Increasing Subsequence is:", longest_increasing_subsequence(arr))

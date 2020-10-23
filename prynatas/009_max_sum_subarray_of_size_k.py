def max_sub_array_of_size_k1(k, arr):
    max_sum = 0
    window_sum = 0

    for i in range(len(arr)-k + 1):
        window_sum = 0
        for j in range(i, i+k):
            window_sum += arr[j]
        max_sum = max(max_sum, window_sum)

    return max_sum

def max_sub_array_of_size_k2(k, arr):
    max_sum = 0
    window_sum = 0
    window_start = 0
    
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k-1:
            max_sum = max(max_sum, window_sum)
            window_sum = window_sum - arr[window_start]
            window_start = window_start + 1

    return max_sum

def max_sub_array_of_size_k(k, arr):
    max_sum = 0

    for i in range(k):
        max_sum += arr[i]

    window_sum = max_sum
    for window_end in range(k, len(arr)):
        window_start = window_end - k
        window_sum = window_sum + arr[window_end] - arr[window_start]
        max_sum = max(max_sum, window_sum)

    return max_sum

print(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])) # 9
print(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])) # 7
def find(arr, n):
    total_sum = n * (n + 1) // 2

    arr_sum = sum(arr)

    miss_num = total_sum - arr_sum

    return miss_num

n = 6
arr = [1, 2, 4, 5, 6]
result = find(arr, n)
print("The missing number is:", result)

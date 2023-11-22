def sum(arr, k):
    num = {}

    pairs = 0

    for i in arr:
        complement = k - i

        if complement in num:
            print(f"Pair with sum {k}: ({complement}, {i})")
            pairs += 1

        num[i] = num.get(i, 0) + 1

    return pairs

arr = [1, 2, 3, 4, 5, 6, 7]
k = 10
result = sum(arr, k)
print("Number of pairs of integers with sum", k, "is", result)

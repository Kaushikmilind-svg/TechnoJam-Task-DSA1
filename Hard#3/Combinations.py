def find(arr, x, combination, result, start):
    if x == 0:
        result.append(list(combination))
        return

    for i in range(start, len(arr)):
        if arr[i] > x:
            
            continue

        combination.append(arr[i])
        find(arr, x - arr[i], combination, result, i)
        combination.pop()

def print_combinations(arr, x):
    result = []
    find(arr, x, [], result, 0)

    if not result:
        print("Empty")
    else:
        print("Unique combinations:")
        for combination in result:
            print(combination)

arr = [2, 3, 4, 5, 6]
sum = 10
print_combinations(arr, sum)

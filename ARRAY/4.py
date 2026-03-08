arr = [1, 2, 3]
result = []

for i in range(len(arr)):
    for j in range(i, len(arr)):
        # arr[i:j+1] creates a new list (the subarray)
        result.append(arr[i : j+1])

print(result) # Output: [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]

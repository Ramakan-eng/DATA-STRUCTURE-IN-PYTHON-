# Example 1:
# Input: N = 6, array[] = {13,46,24,52,20,9}
# Output: 9,13,20,24,46,52
# Explanation: After sorting the array is: 9, 13, 20, 24, 46, 52

arr = [5,4,3,2,1]
n = len(arr)

for i in range(n):
    for j in range(i+1,n):
        if arr[j] < arr[i]:
            arr[i], arr[j] = arr[j], arr[i]

print("sorted array:",arr)
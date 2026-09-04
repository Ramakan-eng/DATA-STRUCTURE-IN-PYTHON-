# Example 1:
# Input:
#  arr[] = {2, 5, 1, 3, 0}  
# Output:
#  5  
# Explanation:
  
# 5 is the largest element in the array.

arr = [2,5,1,3,0]
n = len(arr)

for i in range(1,n):
    key = arr[i]
    j = i -1

    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j = j-1

    arr[j+1] = key

print(arr)    





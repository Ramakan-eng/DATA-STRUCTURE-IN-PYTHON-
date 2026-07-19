# Example 1:
# Input: array[] = {10,5,10,15,10,5};
# Output: 10 15
# Explanation: The frequency of 10 is 3, i.e. the highest and the frequency of 15 is 1 i.e. the lowest.

from collections import defaultdict
arr = [10,5,10,15,10,5]
n = len(arr)


def hashing(arr,n):
    max_val = float("-inf")
    max_element =0
    min_val = float("inf")
    min_element = 0 
    freq_map = defaultdict(int)

    for i in range(n):
        freq_map[arr[i]] +=1
    

    for j in freq_map:
        if freq_map[j] > max_val:
            max_val = freq_map[j]
            max_element = j
        elif freq_map[j] < min_val:
            min_val = freq_map[j]
            min_element = j
    print("maximum key:value:",max_element, ":", max_val)
    print("minimux key:value:",min_element, ":", min_val)
    

hashing(arr , n)
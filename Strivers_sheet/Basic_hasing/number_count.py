# Example 1:
# Input: arr[] = {10,5,10,15,10,5};
# Output: 10  3
# 	            5  2
#                 15  1
# Explanation: 10 occurs 3 times in the array
# 	      5 occurs 2 times in the array
#               15 occurs 1 time in the array

# BROUTE FORCE TECHNIQUE

def freq_arr(arr, n):
   visited_arr = [0] * n

   for i in range(n):
       if visited_arr[i]:
           continue
       count =1
       for j in range(i+1,n):
           if arr[i] == arr[j]:
               visited_arr[j] = 1
               count =count + 1
       print(arr[i],":",count,end=" ")

freq_arr([10,5,10,15,10,0],6)


# BY DICTIONARY 



arr= [10,5,10,15,10,5]
freq = {}
for i in arr:
    if i in freq:
        freq[i] =freq[i]+1
    else:
        freq[i] = 1
print("frequency of words:",freq)



# By defaultdictionary

from collections import defaultdict
def defaultdict_hash(arr,n):
    freq_map = defaultdict(int)

    for i in range(n):
        freq_map[arr[i]] += 1
    
    for key, value in freq_map.items():
        print("frequency by defaultdict : ",key,":",value)


defaultdict_hash([10,5,10,15,10,5,0],7)



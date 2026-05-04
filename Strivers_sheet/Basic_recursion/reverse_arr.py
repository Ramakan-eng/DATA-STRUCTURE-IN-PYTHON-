# Reverse a given Array


# 14

# Problem Statement: You are given an array. The task is to reverse the array and print it.

# Examples
# Input: N = 5, arr[] = {5,4,3,2,1}
# Output: {1,2,3,4,5}
# Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

# Input: N=6 arr[] = {10,20,30,40}
# Output: {40,30,20,10}
# Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.


def reverse(arr):
    n=len(arr)
    reverse_arr =[0] * n
    for i in range(n):

        reverse_arr[i]=arr[n-1-i]
       

      
    print(reverse_arr)
reverse([1,2,3,4,5])

def reverse_itself(num):
    p1 =0 
    n = len(num)
    p2 = n-1
    while p1 < p2:
        
            num[p1],num[p2] =num[p2],num[p1]

            p1 = p1 + 1
            p2 = p2 -1
    print(num)

reverse_itself([1,2,3,4,5])



def reverse_by_func(num):
     num= num[::-1]
    #  print(a)
     print(num)

reverse_by_func([1,2,3,4,5])
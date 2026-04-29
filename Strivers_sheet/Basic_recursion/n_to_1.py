# Print N to 1 using Recursion


# 6

# Problem Description: Given an integer N, write a program to print numbers from N to 1.

# Examples
# Input: N = 4
# Output: 4, 3, 2, 1
# Explanation: All the numbers from 4 to 1 are printed.
# Input: N = 1
# Output: 1 
# Explanation: This is the base case.

def number(num):
    if num <1:
        return
    print(num , end = " ")

    number(num -1)

number(5)
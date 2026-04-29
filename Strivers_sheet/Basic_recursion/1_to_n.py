# Print 1 to N using Recursion


# 15

# Problem Description: Given an integer N, write a program to print numbers from 1 to N.

# Examples
# Input: N = 4
# Output: 1, 2, 3, 4
# Explanation: All the numbers from 1 to 4 are printed.
# Input: N = 1
# Output: 1 
# Explanation: This i

def number(current,num):
    if current > num:
        return
    print(current , end= " ")

    number(current + 1,num)

number(1,5)
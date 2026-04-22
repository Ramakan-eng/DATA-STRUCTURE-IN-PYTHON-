# Problem Statement: Given an integer N, return the number of digits in N.

# Example 1:
# Input:N = 12345
# Output:5
# Explanation:  The number 12345 has 5 digits.
                        
def count(n):
    n = abs(n)
    if n==0:
        print(1)
        return 1
   
    count =0
    while n>0:
        n=n//10
        count = count+1
    print(count)

count(123)
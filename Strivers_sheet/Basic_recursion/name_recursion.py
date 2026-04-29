# Print Name N times using Recursion


# 24

# Problem Description: Given an integer N, write a program to print your name N times.

# Examples
# Input: N = 3
# Output: Ashish Ashish Ashish 
# Explanation: Name is printed 3 times.
# Input: N = 1
# Output: Ashish 
# Explanation: Name is printed once.

def print_name(name,count,n):
    
    if count == n:
        return
    
    print(name)

    print_name(name,count + 1,n)
  
print_name("RK",0,5)




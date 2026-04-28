# Problem Statement:Given an integer N, return true it is an Armstrong number otherwise return false.

# An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
# Examples
# Example 1:
# Input:N = 153
# Output:True
# Explanation: 1^3+5^3+3^3 = 1 + 125 + 27 = 153
                                        
# Example 2:
# Input:N = 371                
# Output: True
# Explanation: 3^3+7^3+1^3 = 27 + 343 + 1 = 371

def armstrong(num):
    n =str(num)
    arm_num = 0
    for i in range(len(n)):
        nums =int(n[i])**3
        arm_num = arm_num + nums
    if arm_num == num:
        print("yes this is armstrong number:",num)
    else:
        print("this is not armstorng number")
        return False
    
armstrong(37)
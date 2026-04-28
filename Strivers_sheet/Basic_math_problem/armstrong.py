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
        print("this is not armstorng number:",num)
        return False
    

def by_digit_armstrong(num):
    copy_arm =num
    arm_num =0
    while num >0:
        digit =num%10 
        arm_num =arm_num + digit**3
        num = num//10
    if arm_num == copy_arm:
        print("Given number is armstrong number:",arm_num)
    else:
        print("given arm number is not armstrong number:",copy_arm )
    
armstrong(37)
by_digit_armstrong(15)
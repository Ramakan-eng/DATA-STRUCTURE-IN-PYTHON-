# Print all Divisors of a given Number


# 17

# Problem Statement: Given an integer N, return all divisors of N.
# A divisor of an integer N is a positive integer that divides N without leaving a remainder. In other words, if N is divisible by another integer without any remainder, then that integer is considered a divisor of N.

# Examples
# Input: N = 36
# Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]  
# Explanation: The divisors of 36 are 1, 2, 3, 4, 6, 9, 12, 18, 36.
# Input: N = 12
# Output: [1, 2, 3, 4, 6, 12]
# Explanation: The divisors of 12 are 1, 2, 3, 4, 6, 12.

def all_diveser(num):
    diviser =1 
    list_div =[]
    while diviser <= num:
        remi = num % diviser
        if remi ==0:
            list_div.append(diviser)
        diviser = diviser + 1
    print(list_div)

def by_sqrt(num):
    div_list =[]

    for  i in range(1,int(num**(1/2))+1):
        if num % i ==0:
            div_list.append(i)
            if i != num//i:
                div_list.append(num//i)
    print(div_list)
all_diveser(16)
by_sqrt(16)

# Sum of first N Natural Numbers


# 9

# Problem Statement: Given a number ‘N’, find out the sum of the first N natural numbers .

# Examples
# Input: N=5
# Output: 15
# Explanation: 1+2+3+4+5=15

# Input: N=6
# Output: 21
# Explanation: 1+2+3+4+5+6=15

# by for loop 

class First_NSum: 
    def by_loop(self,n):
        total = 0 
        for i in range(1,n+1):
            total = total + i
        print(total)
        return total
    
    def by_formula(self ,num):

        total = int(num*(num + 1) / 2)
        print(total)
        return total




obj = First_NSum()
obj.by_loop(5)
obj.by_formula(5)



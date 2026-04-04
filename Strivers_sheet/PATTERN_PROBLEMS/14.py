# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



# A

# AB

# ABC

# ABCD

# ABCDE



# Print the pattern in the function given to you.

class pattern:
    def forteen(self,n):
        
        for i in range(n):
            k=65
            for j in range(i+1):
                print(chr(k),end="")
                k +=1
            print()
p = pattern()
p.forteen(5)
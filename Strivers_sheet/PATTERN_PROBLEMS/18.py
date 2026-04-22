# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



# E 

# D E 

# C D E 

# B C D E 

# A B C D E



# Print the pattern in the function given to you.

class pattern:
    def eighteen(self,n):
        for i in range(n-1,-1,-1):
            k = 65+i
            for j in range(n,i,-1):
                print(chr(k),end="")
                k -=1
            print()
p = pattern()
p.eighteen(3)
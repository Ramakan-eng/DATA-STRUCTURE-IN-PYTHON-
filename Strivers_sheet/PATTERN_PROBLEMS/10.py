# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



# *

# **

# ***

# ****

# *****

# ****

# ***

# **

# *



# Print the pattern in the function given to you.

class pattern:
    def ten(self, n):
        for i in range(1,n+1):
            for j in range(1):
                print("*" *i)
        for i in range(n-1,0,-1):
            for j in range(1):
                print("*" * i)

p = pattern()
p.ten(5)
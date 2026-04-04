# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

# *****
# ****
# ***
# **
# *



class pattern:
    def sixpromplem(self,n):
        for i in range(n):
            for j in range(n,i,-1):
                print("*",end="")
            print()

obj = pattern()
obj.sixpromplem(5)
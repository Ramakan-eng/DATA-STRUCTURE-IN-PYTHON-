# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



# 1 

# 0 1 

# 1 0 1 

# 0 1 0 1 

# 1 0 1 0 1



# Print the pattern in the function given to you.

class pattern:
    def eleven(self,n):
        for i in range(n):
            if i%2 ==0:
                val=1
            else:
                val = 0
            for j in range(i+1):
                print(val,end=" ")
                val = 1-val
            print()
p = pattern()
p.eleven(5)
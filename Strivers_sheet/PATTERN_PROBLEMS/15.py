# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



# ABCDE

# ABCD

# ABC

# AB

# A



# Print the pattern in the function given to you.

class pattern:
    def fifteen(self,n):
        for i in range(n):
            k = 65
            for j in range(n,i,-1):
                print(chr(k),end = "")
                k += 1

            print()

p = pattern()
p.fifteen(5)
# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



# A

# BB

# CCC

# DDDD

# EEEEE



# Print the pattern in the function given to you.

class pattern:
    def sixteen(self,n):
        k=65
        for i in range(n):
            for j in range(i+1):
                
                print(chr(k),end = " ")

            k +=1
            print()
p = pattern()
p.sixteen(5)
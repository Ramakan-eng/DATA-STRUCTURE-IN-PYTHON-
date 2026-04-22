# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:



#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA


# Print the pattern in the function given to you.

class pattern:
    def seventeen(self,n):
        for i in range(n):
            k=65
            print(" " * (2*n - 2 * i),end="")
            for j in range(i+1):
                print(chr(k),end="")
                k+=1
            k=65
            for l in range(1,i+1):
                print(chr(k),end="")
                k+=1
            print()
p = pattern()
p.seventeen(6)
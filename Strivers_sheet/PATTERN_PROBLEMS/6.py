# given below for any value of N. Let's say for N = 5, the pattern should look like as below:

# 12345
# 1234
# 123
# 12
# 1

class pattern:
    def six(self,n):
        for i in range(n,0,-1):
            for j in range(1,i+1):
                print(j,end="")
            print()
obj = pattern()
obj.six(5)
class pattern:
    def sevenpyramid(self,nums):
        for i in range(nums):
            for j in range(i,i+1):
                print(" "*(nums-i-1), "*"*(2*i+1))

p = pattern()
p.sevenpyramid(3)
       
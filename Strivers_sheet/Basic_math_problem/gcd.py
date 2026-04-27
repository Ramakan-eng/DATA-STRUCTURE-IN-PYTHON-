class gcd:
    def gcd_cal(self,a,b):
        
        while b :
            a,b = b,a%b

        print(a)
        return a
    
obj = gcd()
obj.gcd_cal(9,12)

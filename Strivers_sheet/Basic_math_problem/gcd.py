class gcd:
    def gcd_cal(self,a,b):
        
        while b :
            a,b = b,a%b

        print(a)
        return a
    
    def by_broute(self,a,b):
        gcd =1
        if a<b:
            for i in range(1,a):
                if a%i ==0 and b % i ==0:
                    gcd = i
            print(gcd)
            return gcd
        else:
            for i in range(1,b):
                if a%i ==0 and b%i==0:
                    gcd = i
            print(gcd)
            return gcd

    def by_better_approach(self,a,b):
        for i in range(min(a,b),0,-1):
            if a%i ==0 and b%i == 0:
                print(i)
                return i 
obj = gcd()
# obj.gcd_cal(9,12)
obj.by_broute(9,12)
obj.by_better_approach(9,12)

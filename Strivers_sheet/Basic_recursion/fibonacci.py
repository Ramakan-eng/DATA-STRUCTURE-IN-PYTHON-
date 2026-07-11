# Broute force approach

def fibonnaci(num):
    if num == 0:
        print(0)
    elif num ==1:
        print("0,1")
    else: 
        fib =[0] * (num+1)
        fib[0]=0
        fib[1]=1
        for i in range(2,num+1):
            fib[i] = fib[i-1]+fib[i-2]

        print(f"fibonnacci series of {num} is : ")
        print(" ".join(str(n) for n in fib))
# fibonnaci(6)

# Better approach 

def fib(n):
    if n<=1:
        print(n,end=" ")
        return n 
    else:
        last_num= 0

        second_num = 1
        print(f"fibonacci series of the {n} is : ")
        print(last_num,second_num, end = " ")
        for i in range(2,n+1):
            curtent_val = last_num + second_num
            last_num, second_num = second_num , curtent_val

            
    
            print(curtent_val, end = " ")        
        
fib(4)
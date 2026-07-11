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
fibonnaci(6)
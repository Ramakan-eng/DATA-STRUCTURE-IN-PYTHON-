def fibonacci(num):
    a =0
    b=1
    n =0
    while n <= num:
            print(a)
            next = a+b
            a= b 
            b = next
            n = n + 1
            
        

fibonacci(5)
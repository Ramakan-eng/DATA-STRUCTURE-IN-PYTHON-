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
            
# fibonacci(5)

def fibonaccis(N):

    if N <= 1:
        print(f"base case {N}")
        return N
    
    last = fibonaccis(N - 1)   # (N-1)th term
    slast = fibonaccis(N - 2)  # (N-2)th term
    print(f"last {last} and slast {slast} :",last + slast)
    return last + slast

# Driver code
N = 4
print(fibonaccis(N))  
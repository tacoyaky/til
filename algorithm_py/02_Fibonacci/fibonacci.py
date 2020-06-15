import sys

# Calculate Fibonacci sequence
def fib(n):
    if n > 1 :
        # F(n+2) = F(n+1) + F(n)
        # F(n) = F(n-1) + F(n-2)
        return fib(n - 1) + fib(n - 2) 
        
    else:
        # F(0)=0, F(1)=1
        return n

# main
if __name__ == "__main__":
    if len(sys.argv) > 1 :
        arg = sys.argv[1]
        if arg.isdigit() and int(arg) >= 0:
            print(fib(int(arg)))
        else:
            print('err : Argument is invalid.')    
    else:
        print('err : No argument.')

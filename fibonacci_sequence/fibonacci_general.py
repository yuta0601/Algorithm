
def fib(n, a=0, b=1):
    if n < 1:
        return a
    return fib(n-1, b, a+b)

if __name__=='__main__':
    print(f'fib(6): {fib(6)}')
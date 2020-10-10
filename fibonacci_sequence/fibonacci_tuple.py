
def fib(n):
    if n < 1:
        return(0, 0)
    elif n == 1:
        return (0, 1)
    else:
        (a, b) = fib(n-1)
        return (b, a+b)


if __name__=='__main__':
    print(f'fib(6): {fib(6)[-1]}')
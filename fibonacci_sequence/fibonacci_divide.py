# 分割統治法
# トップダウン方式
# 再起的に計算するため計算内容が重複することがある

def fib(n):
    if n < 2:
        return n
    else:
        a = fib(n-1)
        b = fib(n-2)
        c = a + b
        return c


if __name__=='__main__':
    print(fib(6))
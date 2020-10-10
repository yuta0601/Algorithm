# 動的計画法
# ボトムアップ方式
# 計算内容が重複することはないが無駄な計算を行ってしまう可能性がある

def fib(n):
    A = [None] * (n+1)
    A[0] = 0
    A[1] = 1
    for i in range(2, n+1):
        A[i] = A[i-1] + A[i-2]
    return A[n]


if __name__=='__main__':
    print(fib(6))
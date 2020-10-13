
def bubble_sort(target):
    for i in range(0, len(target)-1):
        if modify_order(target, i) == 0:
            break

def modify_order(target, i):
    exchange = 0
    # targetの最終項からi+1まで繰返し
    for j in range(len(target)-1, i, -1):
        if target[j-1] > target[j]:
            target[j-1], target[j] = target[j], target[j-1]
            exchange += 1
    return exchange


if __name__=='__main__':
    A = [3, 2, 9, 4, 8, 1]
    bubble_sort(A)
    print(A)
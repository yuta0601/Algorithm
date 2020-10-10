def bubble_sort(target):
    hikaku = 0
    change = 0
    for i in range(0, len(target)-1):
        exhikaku, exchange = modify_order(target, i)
        hikaku += exhikaku
        change += exchange
    print(f'比較回数:{hikaku}')
    print(f'交換回数:{change}')

def modify_order(target, i):
    hikaku = 0
    change = 0
    for j in range(len(target)-1, i, -1):
        hikaku += 1
        if target[j-1] > target[j]:
            change += 1
            target[j-1], target[j] = target[j], target[j-1]
    return hikaku, change



if __name__=='__main__':
    A = [5, 4, 6, 8, 1, 9]
    bubble_sort(A)
    print(A)
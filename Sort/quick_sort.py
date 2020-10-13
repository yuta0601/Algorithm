def sort(target):
    if len(target) < 2:
        return target
    p = target[0]
    X, Y = divide(p, target[1:])
    return sort(X) + [p] + sort(Y)

def divide(p, target):
    if len(target) < 1:
        return ([], [])
    X, Y = divide(p, target[1:])
    a = target[0]
    if a < p:
        return ([a]+X, Y)
    else:
        return (X, [a]+Y)


if __name__=='__main__':
    A = [40, 3, 1, 23, 48, 22, 64, 3, 13]
    print(f'unsort: {A}')
    A = sort(A)
    print(f'sorted: {A}')
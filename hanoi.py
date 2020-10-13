
def move(k, start, yobi, end):
    if k >= 2:
        move(k-1, start, end, yobi)
    print(f'{start}軸の円盤を{end}軸へ移動')

    if k >= 2:
        move(k-1, yobi, start, end)

if __name__=='__main__':
    move(4, 1, 2, 3)
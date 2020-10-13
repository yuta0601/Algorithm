def insertion_sort(target):
    for i in range(1, len(target)):
        print(f'{target}変換対象：{target[i]}')
        insert(target, i)

def insert(target, i):
    temp = target[i]
    # スタート値: i-1, 終了値: -1, step: -1
    # i-1から0まで逆順に見ていく
    # iのスタート値が1のため終了値を-1にして0まで見るようにしている
    for j in range(i-1, -1, -1):
        # tempより大きい値は右にひとつずらす
        if temp < target[j]:
            target[j+1] = target[j]
        # tempより小さい値が見つかったらその次にtempを入れる
        else:
            target[j+1] = temp
            # これ以上走査する必要がないのでbreak
            break
    # 繰り返し処理を最後まで終了した場合には一番最初にtempを入れる
    else:
        target[0] = temp

if __name__=='__main__':
    A = [6, 3, 8, 5, 7]
    print(f'ソート前:{A}')
    insertion_sort(A)
    print(f'ソート後:{A}')
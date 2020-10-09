
# 選択ソートをコード化
def sort(target):
    # 一番最後の項は実行する必要が無いためlen(target)-1
    for i in range(0, len(target)-1):
        select_min(target, i)

# targetのi番目以降の最小値を見つけi番目の値より小さい場合交換する
def select_min(target, i):
    min = i
    # rangeは終了値実行jされないためlen(target)で問題無い
    for j in range(i+1, len(target)):
        # i+1番目以降の最小値のインデックスを取得
        if target[min] > target[j]:
            min = j
    target[i], target[min] = target[min], target[i]

if __name__=='__main__':
    A = [8, 4, 3, 9, 6]

    sort(A)

    print(A)
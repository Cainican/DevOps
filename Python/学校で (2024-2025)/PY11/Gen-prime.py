##################################
#   P. 146 素数を返すイテレータ   #
#          Gen-prime.py          #
##################################

# 素数を返すイテレータ
def genPrime(maxnum):
    num = 2
    while (num <= maxnum):          # 指定の数(50)まで繰り返す
        is_prime = True             # boolean
        for i in range(2, num):
            if (num % i) == 0:      # 割切れるか
                is_prime = False    # 割り切れたので素数ではない
                break

        if is_prime: yield num  # is_primeがTrueなら
        num += 1                # 素数に追加

it = genPrime(50)

# 画面に出力
for i in it:
    print(i, end=",")
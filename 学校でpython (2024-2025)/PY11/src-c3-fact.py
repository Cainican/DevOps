######################
#   src/c3/fact.py   #
######################

def fact(n):
    # 引数が0になったら１を返す
    if n == 0:
        return 
    
    # それ以外の場合は再帰的にfact()関数を呼ぶ
    else:
        return n * fact(n - 1)

print(fact(3))
print(fact(5))
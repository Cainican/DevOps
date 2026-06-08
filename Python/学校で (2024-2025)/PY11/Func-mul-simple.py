##########################
#   Func-mul-simple.py   #
##########################

# かけ算を行うだけの関数を定義
def mul(a,b):

    # もらった引数2つで掛け算を行い,
    # 結果を返す
    return a * b

# 定義した関数を使う
x = int(input("数値1を入力: "))
y = int(input("数値2を入力: "))

# Input din funktioner in (x, y)
# for at fortælle hvad den skal udregne
ans = mul(x,y)

print("{0} x {1}の答えは{2}です。".format(x,y,ans))
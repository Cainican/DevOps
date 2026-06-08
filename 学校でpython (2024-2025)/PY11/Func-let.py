###################
#   Func-let.py   #
###################

# 関数を定義
def mul_func(a, b):   # aとbをかけ算する関数
    return a * b

def div_func(a, b):   # aとbで割る関数
    return a / b

# mul_func関数を変数に代入 ---(1)
func = mul_func   # 関数(オブジェクト)を代入

def calc_5_3(func):
     return func(5, 3)    # mul_func(5, 3)と同じ
                          # 関数mul_funcを引数と
                          # 渡されたcalc_5_3()では

# 代入した変数で関数を使う ---(2)
result = func(2, 3)   # mul_func(2, 3)と同義になる

print(result)   # 表示結果


# div_func関数を変数に代入する場合 ---(3)
func2 = div_func
result = func2(10, 5)
print(result)   # 表示結果 -> 2.0
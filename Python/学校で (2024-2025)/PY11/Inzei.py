################
#   Inzei.py   #
################

# 印税を計算する関数 ---(1)
def calc_royalty(price, sales, per):
    rate = per / 100                    # 印税率(ここでは10)を100で割れる
    ro = int(price * sales * rate)      # 定価と発行部数と印税率を掛けて、それを整数にする
    return ro

# ユーザーから情報を入力してもらう --- (2)
i = input("定価は?")
price = int(i)

i = input("発行部数は?")
sales = int(i)

i = input("印税率(パーセント)は?")
per = float(i)

# 結果を表示する ---(3)
v = calc_royalty(price, sales, per)     # calc_rolalty() 関数を呼び出す
print("印税は、",v,"円です")
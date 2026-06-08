################################
#  円 to DKクロナ変換プログラム　 #
#     Exchange jpy to usd      #
################################

# 1000円 = 46.50 DKK
# 変換するjpyを入力させる
jpy = int(input("変換する金額(円): "))

# 0006 ー> # 0036 として入力させる
# かわせ
# 為替レートの入力 (JPY to DKK)
rate = float(input("為替レートの入力 (JPY to DKK): "))

# Du skriver selv valuta omregningen
# JPY to DKK
DKK = jpy / rate

# 結果の表示 (DKKは小数点2ケタです)
print("{0}円は{1}DKKです.".format(jpy, round(DKK,2)))
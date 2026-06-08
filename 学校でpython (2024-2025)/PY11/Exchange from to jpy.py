##################################
#   Valuta exchange USD to JPY   #
##################################

# jpy to usd, or usd to jpy を選択させる
print("\n為替変換プログラム\n")
print("1. JPY to USD")
print("2. USD to JPY\n")

# どっちから選択してください
currency = int(input("処理を選択して下さい: "))

# 入力された番号によって処理を分ける
if currency == 1:
    # 変換するjpyを入力させる
    jpy = float(input("変換する金額(円): "))

    # かわせ
    # 為替レートの入力 (JPY to USD)
    rate = float(input("為替レートの入力 (JPY to USD): "))

    # Du skriver selv valuta omregningen
    # JPY to USD
    USD = jpy / rate
    # 結果の表示 (DKKは小数点2ケタです)
    print("{0}円は{1}USDです.".format(jpy, round(USD,2)))

elif currency == 2:
    # 変換するusdを入力させる
    usd = float(input("変換する金額(円): "))

    # かわせ
    # 為替レートの入力 (JPY to DKK)
    rate = float(input("為替レートの入力 (USD to JPY): "))

    # Du skriver selv valuta omregningen
    # JPY to DKK
    JPY = usd * rate

    # 結果の表示 (DKKは小数点2ケタです)
    print("{0}USDは{1}円です.".format(usd, int(JPY)))

else:
    print("１か２選んでください")
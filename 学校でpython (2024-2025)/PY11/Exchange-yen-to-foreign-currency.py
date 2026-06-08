###########################################
#   Exchange yen to foreign currency.py   #
###########################################

# Defining the valuta
def exchange(amount, cur_kinds, p_num):
    usd = 145.5
    eur = 48.2
    cny = 20.2
    krw = 0.1

# Tell python how to exchange the currencies
    if p_num == 1:
        if c_amount == 1:
            c_amount = amount / usd
    
        elif cur_kinds == 2:
            c_amount = amount / eur
    
        elif cur_kinds == 3:
            c_amount = amount / cny
    
        elif cur_kinds == 4:
            c_amount = amount / krw

# Do the same, exchange the other way around
    elif p_num == 2:
        if cur_kinds == 1:
            c_amount = amount * usd
        
        elif cur_kinds == 2:
            c_amount = amount * eur
    
        elif cur_kinds == 3:
            c_amount = amount * cny
    
        elif cur_kinds == 4:
            c_amount = amount * krw
    return c_amount

# Make it a loop, so it goes on, until I tell it to stop
while True:
    print("1. 日本円→外貨")
    print("2. 外貨→日本円")
    print("9. 終了\n")

    p_num = int(input("処理を選択してください: "))

    if p_num == 9:
        break

    print("\n変換する外貨を選択してください。")
    print("""
1. USドル(USD)
2. ユロ(EUR)
3. 元(CNY)
4. ウォン(KRW)
""")

    # Ask user to chose currency
    cur_kinds = int(input("番号: "))

    # Ask user for amount
    amount = float(input("金額を入力してください: \n"))

    # 関数の呼び出し
    c_amount = exchange(amount, cur_kinds, p_num)

    unit1 = "円"

    if cur_kinds == 1:
        unit2 = "ドル"

    elif cur_kinds == 2:
        unit2 = "ユロ"

    elif cur_kinds == 3:
        unit2 = "元"

    elif cur_kinds == 4:
        unit2 = "ウォン"
    
    if p_num == 1:
        print("{0}{1}は{2}{3}です。".format(amount,unit1,c_amount,unit2))
    
    elif p_num == 2:
        print("{0}{1}は{2}{3}です。".format(amount,unit2,c_amount,unit1))
    
    print()
#############################################
#   課題07-PY11A084-09-エリアッセン カスパ   #
#############################################

# minimum 1, 2, 3 and 9
# try to do all of them!

# 1 Hello world
def hello_world():
    print("Hello world!")

# 2 指定数
def print_sum():
    prnsum = int(input("指定数を入力: "))
    total_sum = 0

    for i in range(1, prnsum + 1):
        total_sum += i

    print("{0}から{1}までの合計は{2}です".format(1, prnsum, total_sum))

# 3 小文字大文字になる
def print_upper():
    capslock = input("英文字を選択: ")
    cap_upper = capslock.upper()
    print("更新前は: {0}".format(capslock))
    print("更新後は: {0}".format(cap_upper))

# 4 "*"で四角を作ると
def print_square():
    square = int(input("数値を入力: "))
    print("*" * square)
    for _ in range(square - 2):
        print("*" + " " * (square - 2) + "*" )
    print("*" * square)

# 5 数える (加算, 減算, 乗算, 除算)
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "エラー: ゼロ除算"

def print_calc():
    calc1 = int(input("数値1を入力: "))
    calc2 = int(input("数値2を入力: "))
    calc = int(input("演算を入力 (0: 加算, 1: 減算, 2: 乗算, 3: 除算): "))


    if calc == 0:
        print(calc1, "+", calc2, "=", add(calc1, calc2))
    
    elif calc == 1:
        print(calc1, "-", calc2, "=", subtract(calc1, calc2))
    
    elif calc == 2:
        print(calc1, "*", calc2, "=", multiply(calc1, calc2))

    elif calc == 3:
        # Fixed typo here: calc1 should be calc2
        print(calc1, "/", calc2, "=", divide(calc1, calc2))
    
    else:
        print("0から3までの数値を入力して下さい")

# 9 終了
def print_done():
    print("終了・・・")



while True:
    print("\n1. Hello world!と出力する")
    print("2. 1から指定数までの合計を入力する")
    print("3. 英文字をすべて大文字に変換して出力する")
    print("4. 指定数を辺の長さとした四角形を出力する")
    print("5. 四則演算を行う")
    print("6. カンマ区切りデータを入力し、平均を求める")
    print("9. 終了" "\n")


    num = int(input("処理を選択: "))

    if num == 1:
        hello_world()

    elif num == 2:
        print_sum()

    elif num == 3:
        print_upper()

    elif num == 4:
        print_square()

    elif num == 5:
        print_calc()

    elif num == 9:
        print_done()
        break
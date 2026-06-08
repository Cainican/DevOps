#############################################
#   Kadai0801-IT11A084-09-Eliassen Casper   #
#       Guess the number game 1-100         #
#############################################

# ランダマイザーを入力
import random

# 数値の範囲をパソコンに伝える
range = random.randint(1,100)

print("1-100までの数字当てゲーム\n")

guesses = 0

# ルーブを作る
while True:
    guess = int(input("1-100までの数字を入力 (999で終了): "))

    if guess == 999:
        print("\nゲームを終了します")
        break

    if guess > 100:
        print("1-100まで番号を入力してください\n")

    elif guess < range:
        print("もう少し大きい\n")
        guesses += 1

    elif guess > range:
        print("もう少し小さい\n")
        guesses += 1

    else:
        print("あたり!\n")
        print("推測は" + str(guesses) + "です\n")
    
        # 推測した後にランダム化するようにパソコンに指示します
        # すいそく
        range = random.randint(1, 100)
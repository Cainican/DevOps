##################################
#   P. 149 Try-exceptプログラム   #
#           Try-BMI              #
##################################

# BMI判定(例外処理あり版)
# ユーザーから正しい値を得てBMIを計算
while True:
    try:        # breakするまで繰り返す
                # 入力
        weight = float(input("体重(kg): "))
        height = float(input("身長(cm): "))

        # BMIの計算
        height = height / 100 # に値す
        bmi = weight / (height * height)
        break

    except:     # エラーの時はここに来る(全エラー供通)
        # 再入力を足す
        print("入力ミスがあります。再度入力してください。")

# BMIの値から結果を判定
result = ""
if bmi < 18.5: result = "痩せ型"
elif bmi < 25: result = "標準体重"
elif bmi < 30: result = "肥満(軽)"
else: result = "肥満(重)"

# 計算結果を表示する
print("BMI: ", round(bmi, 1))
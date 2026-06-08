##################################
#   P. 151 Try-exceptプログラム   #
#         Error-types            #
##################################

s = input("体重: ")
try:
    v = 100 / float(s)
    print(v)

except ValueError as e:
    # 何も入力がなかった時,数値じゃないものが入った時
    print(e)

except ZeroDivisionError as e:
    print(e)

except:
    print("その他のエラー")
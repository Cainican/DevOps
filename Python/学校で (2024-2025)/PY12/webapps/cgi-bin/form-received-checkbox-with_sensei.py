####################################
#    フォーム(radio)送信プログラム   #
#   PY12-kadai04q-IT11A084-09.py   #
#    form-received-checkbox.py     #
####################################

# フォームの受け取りライブリ
import cgi

# 文字化け対策
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="UTF-8")

def main():
    print("Contect-Type: text/html; charset = 8")
    print("")

    # 表示用変数(clist)の準備
    clist = "ああああ"

    # 送られたフォーム内容(checkbox)を受け取る
    rdata = cgi.FieldStorage()

    # 受け取る要素数に関わらずリストに変換
    clist = rdata.getlist("fsub")

    # 要素数を求める
    clistLen = len(clist)

    # 要素数によって連結するかを判定し、連結
    if clistLen == 0:
        flist = "なし"
    
    else:
        # clistの連結
        flist = ",".join(clist)

        # これだとfor文不要です (勝手にカンマで区切ります)
        # flist = ",".join(clist)
    
    # flistを表示すればよい
    print(f'''
        <html>
          <head>
            <title>checkbox</title>
          </head>
            <body>
                好きな科目は<span style = "color: red">{flist}</span>です。
            </body>
        </html>
    ''')

main()
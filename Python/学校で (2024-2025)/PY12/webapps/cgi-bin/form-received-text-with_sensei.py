####################################
#    フォーム(radio)送信プログラム   #
#   PY12-kadai04q-IT11A084-09.py   #
#      form-received-text.py       #
####################################

# フォーム受け取りライブリの準備
import sys

# 文字化け対策
import sys, io, cgi
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="UTF-8")

def main():
    # 文字化け対策
    print("Contect-Type: text/html; charset = 8")
    print("")

    # 送られたフォームの内容を受け取る
    rdata = cgi.FieldStorage()
    rvalue = rdata.getvalue("tbtest", default = "なし")

    print(f'''
        <html>
          <head>
            <title>text</title>
          </head>
            <body>
                <p>受け取ったのは「{rvalue}」です。
            </body>
        </html>
    ''')

main()
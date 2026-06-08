####################################
#    フォーム(radio)送信プログラム   #
#   PY12-kadai04q-IT11A084-09.py   #
#       form-submit-text.py        #
####################################

# 文字化け対策
import sys
import io
import cgi

# 文字化け対策ここまで
def main():
    # 文字化け対策
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="UTF-8")
    print("Contect-Type: text/html; charset = 8")
    print("")

    # htmlを表示
    print(f'''
        <html>
          <head>
            <title>text</title>
          </head>
            <body>
                <form action = "form-received-text.py">
                    <input type = "text" name = "tbtest" maxlength = 30 placeholder = "ここに値を入力してください" />
                    <input type = "submit" value = "送信" />
                </form>
            </body>
        </html>
    ''')

main()
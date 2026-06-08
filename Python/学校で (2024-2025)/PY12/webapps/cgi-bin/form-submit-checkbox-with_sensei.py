####################################
#    フォーム(radio)送信プログラム   #
#   PY12-kadai04q-IT11A084-09.py   #
#     form-submit-checkbox.py      #
####################################

# 文字化け対策
import sys, io, cgi

def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="UTF-8")
    print("Contect-Type: text/html; charset = 8")
    print("")

    # htmlを表示
    print(f'''
        <html>
          <head>
            <title>checkbox</title>
          </head>
            <body>
                <h1>好きな科目は?</h1>
                <input type = "checkbox" name = "fsub" value = "py12>PY12<br>
                <input type = "checkbox" name = "fsub" value = "py12>CS12<br>
                <input type = "checkbox" name = "fsub" value = "py12>CT12<br>

                <input type = "submit" value = "送信">
            </body>
        </html>
    ''')

main()
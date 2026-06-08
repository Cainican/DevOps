##################################
#   フォーム
#      form-submit-text.py       #
##################################

# 文字化け対策
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print("Content-Type:text/html;charset=utf-8")

# 文字化け対策ここまで

def main():
    print("Content-Type: text/html; charset=utf-8")
    print("")

    print(f'''
        <html>
          <head><title>text</title></head>
          <body>
            <form action = "form-received-text.py">
                <input type = "text" name = "tbxtest" maxlength = 30 placeholder = "ここに値を入力してください" />
                <input type = "submit" name = "test" value = "送信" />
            </form>
          </body>
        </html>
    ''')
main()
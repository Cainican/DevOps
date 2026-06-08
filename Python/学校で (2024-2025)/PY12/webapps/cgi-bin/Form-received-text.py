##################################
#   フォーム(text)受信プログラム   #
#     Form-received-text.py      #
##################################

# !/usr/bin/env py
import cgi

# 文字化け対策
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 文字化け対策ここまで
print("Content-Type:text/html;charset=utf-8")
print("")

def main():
    # 送られたフォームの内容を受け取る
    rdata = cgi.FieldStorage()
    rvalue = rdata.getvalue("tbxtest", default="なし")

    print(f'''
        <html>
        <head><title>text</title></head>
        <body>
          <p>受け取ったのは{rvalue}です。
        </body>
        </html>
    ''')
main()
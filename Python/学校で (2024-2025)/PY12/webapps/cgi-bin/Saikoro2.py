##################################
#   P. 219 Webサイコロプログラム   #
#         Saikoro2.py            #
##################################

# !/usr/bin/env py
# 文字化け (Kakugen.pyからコピーして)
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import random

# ここもKakugen.pyからコピー
print("Content-Type:text/html;charset=utf-8")
print("")

# ここからが本題です
no = random.randint(1, 6)
print("""
<html>
<head><title>Dice</title></head>
<body>
    <h1><img src="../images/Dice/{num}.jpg" alt="dice">{num}です</h1>
</body>
</html>
""".format(num = no))

# no = random.randint(1, 6)
# noで選ばれたサイコロの画家パスを相対パスで取得
# image_path = str(f"../images/Dice/{num}.jpg")
# htmlで出力する
# print("""
# <html>
# <head><title>Dice</title></head>
# <body>
#     <p><img src={0}>です</p>
# </body>
# </html>
# """.format(image_path))
##################################
#   P. 219 Webサイコロプログラム   #
#          Saikoro.py            #
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
      <h1>{num}です</h1>
</body>
</html>
""".format(num = no))
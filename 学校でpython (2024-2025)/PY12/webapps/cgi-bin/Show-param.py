#################################
#   P. 220 URLパラメータの取得   #
#        Show-param.py          #
#################################

# 文字化け対策
import cgi
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 文字化け対策ここまで

print("Content-Type: text/html; charset=utf-8")
print("")

# パラメータの取得する (key = 値)
param = cgi.FieldStorage()

# パラメータにmodeがあればその値を取得し、なければ"ない"を返す
mode = param.getvalue("mode", default="ない")

print(f'''
<html><head><meta charset="utf-8"></html><body>
    mode = {mode}
</body>
</html>''')
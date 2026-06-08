# importされると、モジュールの
# プログラム全てが実行される
import my_module
import my_module # ただし、最初の1回のみ

# importされると、モジュール全ての
# メンバ(変数/関数/クラス)が使える
print(my_module.a)
my_module.myfunc()

# fromを使っても同じように全てが実行される
from my_module2 import myfunc
myfunc()

# 変数も読み込める
from my_module2 import a
print(a)
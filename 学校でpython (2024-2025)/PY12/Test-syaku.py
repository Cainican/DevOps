########################
#   P. 157 モジュール   #
#    Test-syaku.py     #
########################

# モジュールのインポート
import Syaku

# モジュールの関数を使う
v = Syaku.syaku_to_cm(10)
print("10尺=", v, "cm")

v = Syaku.syaku_to_cm(20)
print("20尺=", v, "cm")

# 追加した関数(syaku_to_m(syaku))を実行
v = Syaku.syaku_to_m(10)
print("10尺=", v, "m")
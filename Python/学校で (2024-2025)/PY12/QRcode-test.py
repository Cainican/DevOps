######################
#   QRcode.test.py   #
#      P. 167        #
######################

# パッケージをインポート
import qrcode

# QRコートを生成
img = qrcode.make("https://www.youtube.com/")

# ファイルに保存
img.save("qrcode-test.png")
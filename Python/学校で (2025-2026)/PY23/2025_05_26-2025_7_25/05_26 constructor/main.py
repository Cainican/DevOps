# コンストラクタ
# インスタンス化の際に動作するメソッド
# 初期化の用途にて利用される
# 「定義書式」
# def __init__(self):
class User:
  def __init__(self):
    print('コンストラクタ')

# インスタンス化
user = User()
      # ↑これで、コンストラクタが動作する

# コンストラクタ & 引数
class User:
  def __init__(self, a):
    print(a)

user = User('abc')

# コンストラクタ & 戻り値
# →コンストラクタにて、returnは記述しない
class User:
  def __init__(self):
    pass
    # return 1 ←これはありえない
    return # ←あったとしても、これくらい

user = User()
print(user)


# Member
# 物が持っている特性のこと
# 次の2つに分かれる
# ・属性…アトリビュート。
#     その物が持つ、データの事。※名詞
# ・振る舞い…メソッド
#     その物が持つ、処理の事。※動詞

# 振る舞い(メソッド)
# [定義書式]
# def メソッド名(self [, 引数[, 引数...]]):
class User:
  # ここで関数を定義すれば、
  # それがメソッドとなる
  def hello(self):
    print("Hello")

# メソッド呼び出し
# [書式]
# インスタンス変数. メソッド名()
# ※こっちにselfは不要

user = User()
user.hello()
# メソッド(変数)呼び出しは、「小括弧」が必須

# 引数
class User:
  def hello(self, name):
    #第1引数のselfは必須
    #第2数以降に、任意引数を記述する
    print(f'hello {name}')

user = User()
user.hello('s水')

# 戻り値
class User:
  def hello(self):
    return 'hello'

user = User()
print(user.hello())
# 因※みに、returnが無い場合は、
# noneが返却される

# メソッドは複数
class User:
  def a(self):
    print('a')

  def b(self):
    print('b')

user = User()
user.a()
user.b()

# 同ーメソッド名は後方優先
# やらないけど、言語仕様上は動く

class User:
  def a(self):
    print('a')

  def a(self):
    print('b')

user = User()
user.a()
# アトリビュート
# 物が持つ、データの事
# 「定義書式」
# def __int__(self):
#    コンストラクタ上で
#    selfを用いて定義する
#    self.アトリビュート名１ = 初期値
#    self.アトリビュート名２ = 初期値 # ※必要数分定義

# self…自分。自己
# ということで、インスタンス化によって
# 出来上がった物の、その物"自身"を表す
# のがself

class User:
  def __init__(self):
    self.id = 0
    self.name = 'no name'
    self.address = ''
    tel = '090' # self.が無いと、ローカル変数

# アトリビュート値の繰作
# [利用書式]
# インスタンス変数.アトリビュート名

user = User()

print(user.id)
print(user.name)
print(user.address)
# print(user.tel) # ←これは見えない

# 代入式で、外部から値の設定も可能
user.id = 123
user.name = 'abc'
user.address = '東京'
print(user.id, user.name, user.address)

# アトリビュートはコンストラクタで定義が基本
# でも、言語仕様的には、コンストラクタで無くても可
# (保守上やらない方が良い)
class User:
  def a(self):
    self.id = 0
    self.name = 'no name'
    self.address = ''

user = User()
# print(user.id)    # そんな属性は無いとエラー
user.a()            # aメソッドを読んで
print(user.id)      # 初めて使えるようになる。→やらない方が良い
                    # →__init__でやるべき

# また、外部からのアトリビュート追加も可
# これも、保守上、やらない方が良い
user.age = 20
print(user.age)
user.nama = "aaa"
print(user.name)
del user.nama # delで削除も可能
# print(user.nama) # もう無いので、エラー

# コンストラクタ引数にて初期化
class User:
  def __init__(self, id, name):
    self.id = id
    self.name = name

user1 = User(20000, 'aaa')
user2 = User(25000, 'bbb')

# アトリビュートはインスタンス毎に
# 保持される
print(user1.id)
print(user1.name)

print(user2.id)
print(user2.name)

# 保持されているデータ(アトリビュート)は、
# 自分の持ち物なので、自分で使える
# (自メソッドから繰作可能)
class User:
  def __init__(self, id, name):
    self.id = id
    self.name = name

  def print_name(self):
    print(f'私の名前は{self.name}です')

user1 = User(20000, 'aaa')
user1.print_name()

# アトリビュートの使用指針
#   その物が保持し続ける必要があるデータ
#   のみアトリビュートとする
#   ※基本はローカル変数
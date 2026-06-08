# インスタンスメソッドとクラスメソッド
# インスタンス(実体)に依存しているメソッドと、
# クラスに依存しているメソッド。
# 言い換えると、インスタンスの持ち物か、クラスの持ち物かの違い。

# インスタンスメソッド
# インスタンス(実体)の持ち物なので、
# インスタンス変数.メソッド名()にて呼び出す。
# ※今まで作成してきたメソッド。
# [定義書式]
# def method_name(self):
# 利用例）
# my_class = MyClass()
# my_class.method_name()    # 呼び出しにインスタンス変数が必須。

# クラスメソッド
# クラスの持ち物なので、
# クラス名.メソッド名()にて呼び出せる。
# [定義書式]
# @classmethod              ※デコレーター必須
# def method_name(cls):     ※第1引数必須。clsという名前は慣例。
# [利用書式]
# MyClass.method_name()     # 呼び出しにインスタンス変数は不要。※クラスの持ち物なので。
class User:
  def instance_method(self):
    print(1)

  @classmethod
  def class_method(cls):
    print(2)

User.class_method()         # で呼べる
# User.instance_method()    # インスタンス無しで、インスタンスメソッドは呼べない

user = User()
user.instance_method()
user.class_method()

# ポイント
# インスタンスメソッドは、
# 出来上がったインスタンスの持ち物
# クラスメソッドは、
# インスタンスに関係なく、
# クラス自体の持ち物

class User:
  def im(self):
    print(1)

  def im2(self):
    # インスタンスメソッド内から
    # インスタンスメソッドは呼べる
    self.im()
    print(2)

    # クラスメソッドも呼べる
    print(2)

  @classmethod
  def cm(cls):
    print(100)

  @classmethod
  def cm2(cls):
    print(200)

    # クラスメソッド内から
    # クラスメソッドは呼べる
    User.cm()
    cls.cm()    # ↑と一緒

    # クラスメソッド内から
    # インスタンスメソッドは呼べない
    cls.im()

user = User()
user.im2()

User.cm()
User.cm2()
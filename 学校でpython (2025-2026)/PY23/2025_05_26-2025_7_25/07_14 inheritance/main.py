# インヘリタンス(継承)
# オブジェクト指向3大要素の2つめ
# あるクラスの性質を別のクラスに
# 引き継げる仕組み
# 一言で言うと、コピペは止めて、
# 差分だけ作ろうよ

# [継承]書式
# class クラス名(継承元クラス名)
class A:
  def a(self):
    print('a')

# Aの性質を継承する
class B(A):
  pass

b = B()
b.a()

# Aクラスの性質(メソッド)をBクラスに
# 引き継いで(継承して)いるので、
# Bクラスの持ち物にaメソッドがある

# アトリビュートも引き継がれる
class A:
  def __init__(self):
    self.id = 0

class B(A):
  pass

b = B()
print(b.id)

# 基本、親は１つで子は複数の関係
class A:
  def a(self):
    print('a')

class B(A):
  def b(self):
    print('b')

class C(A):
  def c(self):
    print('c')

b = B()
b.a()
b.b()

c = C()
c.a()
c.c()

# [用語]
# 継承元を特に、
# ・スーパークラス
# ・上位クラス
# ・親クラス
# と言う

# 継承元を特に、
# ・サブクラス
# ・下クラス
# ・子クラス
# と言う

# オーバーライド
# 上書き。スーパークラスのメソッドを、
# サブクラスで上書きすることができる
# ※正しくは、「奪い」
class A:
  def a(self):
    print('a')

class B(A):
  pass

b = B()
b.a()

class B(A):
  # 同一メソッドを、別途定義すれば、
  # オーバーライドとなる
  def a(self):
    print('b')

b = B()
b.a()

# サブクラスから
# スーパークラスのメソッドを
# 呼び出せる
# 「書式」
# super().メソッド名()
class B(A):
  def b(self):
    super().a()

    # self.でも行ける
    self.a()

b = B()
b.b()

# super 実用例1)
class B(A):
  # 同一メソッドを、別途定義すれば、
  # オーバーライドとなる
  def a(self):
    super().a()   # 親の元のaのメソッド
    print('b')

b = B()
b.a()

# super 実用例2)
class A:
  def __init__(self, id):
    self.id = id

class B:
  def __init__(self, name):
    self.name = name

b = B('aaa')
print(b.name)
# print(b.id)   # コンストラクタがオーバーライドされたのでidがない

class B(A):
  def __init__(self, id, name):
    self.id = id    # 親と同じ処理を書く → 悪手
    self.name = name

b = B(123, 'abc')
print(b.id, b.name)

# ↑で、要件は満たされるけど、
# self.id = idは冗長。コピーいや
# また、いっぱいアトリビュートが
# あった場合に面倒
# よって、super()

class B(A):
  def __init__(self, id, name):
    # 親のコンストラクタ呼び出し
    super().__init__(id)
    self.name = name

b = B(123, 'abc')
print(b.id, b.name)

# 継承は代々引き継げる
class A:
  def a(self):
    print(1)

class B(A):
  def b(self):
    print(2)

class C(B):
  def c(self):
    print(3)

c = C()
c.a()
c.b()
c.c()

# 多重継承が可能
# →複数の親OK
class A:
  def a(self):
    print(1)

class B:
  def b(self):
    print(2)

# 継承元として、カンマで複数指定が可能
class C(A, B):
  def c(self):
    print(3)

c = C()
c.a()
c.b()
c.c()
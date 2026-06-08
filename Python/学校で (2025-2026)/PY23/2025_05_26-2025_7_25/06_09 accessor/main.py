# アクセッサ
# private(外部非公開)アトリビュートに
# アクセスする専用のメソッド
# 取得するメソッドをゲッター(getter)
# 設定するメソッドをセッター(setter)
# という
class User:
  def __init__(self):
    self.__id = 40000
    self.__name = 'a'

  # idのゲッター
  def get_id(self):
    return self.__id
  
  # idのセッター
  def set_id(self, value):
    self.__id = value

  # nameのゲッター
  def get_name(self):
    return self.__name
  
  # nameのセッター
  def set_name(self, value):
    self.__name = value

user = User()
print(user.get_id())
print(user.get_name())

user.set_id(49999)
user.set_name('b')

print(user.get_id())
print(user.get_name())

# ゲッターのみ作成することにより、
# 読み取り専用とすることが可能。
# ※セッターのみの作成は無い。

# おまけ
# アクセッサの必要性
# オブジェクト指向のお作法として、アトリビュートはprivateにする。
# アクセスするにはアクセッサを用意する。

# アクセッサ、つまりメソッド化することにより、以下の効能が生まれる。
# ①設定値のバリデーション(検証)を組み込むことができる。
# ②読み取り専用を実現することができる。
# ③内部的にアトリビュート名が後に変更されたとしても、
# 公開されているのはアクセッサのメソッドのため、
# アクセッサ(メソッド)名の変更が掛からなければ、
# 利用サイドのプログラムに影響を及ぼさない。

# プロパティ
# アクセッサをメソッドの形式で呼び出すのではなく、
# アトリビュートの形式で呼び出せる様にする仕組み。

# デコレーターを使って
# アクセッサを簡単に使える
# 様にする
class User:
  def __init__(self):
    self.__id = 40000
    self.__name = 'a'

    # ゲッター
  @property
  def id(self):
    return self.__id

  # セッター
  @id.setter
  def id(self, value):
    self.id = value

    # ゲッター
  @property
  def name(self):
    return self.__name

  # セッター
  @name.setter
  def name(self, value):
    self.name = value

user = User()
print(user.id)

user.id = 50000
print(user.id)
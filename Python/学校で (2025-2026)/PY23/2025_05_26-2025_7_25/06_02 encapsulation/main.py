# カプセル化
# オブジェクト指向3大要素
# の内の1つ
# 次の2つの意味合いがある
# 1. 属性と振る舞いを、一つの
#   まとまりとして管理することが
#   できる
# 2. メンバ(アトリビュート&
#   メソッド)を隠蔽する

# [隠蔽書式]
# 各々の定義名称の開始を、
# アンダーバー2つとする
class User:
  def __init__(self):
    self.id = 20000
    self.name = 'aaa'
    self.__privateAttribute = 123
    self.__bbb = 'bbb'

  def a(self):
    # 隠蔽されても、自身(self)で
    # あれば、アクセスできる
    self.__bbb = 'bbb'
    self.__b()

  def __b(self):
    print('private method b')

user = User()
print(user.id)
print(user.name)
# print(user.__privateAttribute)  見えない
# print(user.__bbb)               見えない
user.a()
# user.__b()                      見えない

# おまけ。
# 一般的な言語には情報の公開範囲を制御するアクセス修飾子なるものが存在する。
# 例）public…外部公開 private…外部非公開
# ※pythonには無い。

# おまけ
# Double underscoreを略してDunder(ダンダー)という。

# ポイント
#   極力隠蔽し、不必要な情報を外部に公開しないこと。
#     →保守性向上
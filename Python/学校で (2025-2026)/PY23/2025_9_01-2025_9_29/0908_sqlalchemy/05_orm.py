from sqlalchemy import create_engine, String, func, or_, asc, desc
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, String, func, desc
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
from typing import Optional
db_path = r'C:\PY23\2025_9_01-2025_9_29\0908_sqlalchemy\user2.db'
# engineの作成(DB接続の必要情報定義)
engine = create_engine(
  f'sqlite:///{db_path}',
  echo=True   # 裏で動作しているSQL文を出力する
)

# モデルの元クラスを作成
class Base(DeclarativeBase):
  pass

# Baseクラスを継承して、テーブル用のクラスを定義する。
class User(Base):
  __tablename__ = 'user'

  id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
  name: Mapped[str] = mapped_column(String(50))
  age: Mapped[int]    # 特に指定がなければmapped_columnは不要。※= Columnは古い。
  address: Mapped[Optional[str]]  # Optionalでnull許容（defaultはNOT NULL）

  # memo:実際に実行されるCREATE文に AUTO INCREMENT の記載がないが、
  # 問題はない。これは、SQLiteが、INTのPRIMARY KEYは自動的に
  # AUTO INCREMENTの扱いになるという仕様による。
  # なので、「, autoincrement=True」自体も不要だが、
  # もし自動採番したくない場合には、これをFalseとする必要がある。

# てーぶるの生成
Base.metadata.create_all(bind=engine)

# 登録
with Session(engine) as session:
  user = User(name = 'b', age = 21, address = '神奈川')
  session.add(user)
  session.commit()

# 取得
with Session(engine) as session:
  # session.query を使って、1行ずつ取得する。
  for user in session.query(User):
    print(user.id, user.name, user.age, user.address)

  # .all()付与で、全件一気取得。    -> SEMUA nye
  users = session.query(User).all()
  for user in users:
    print(user.id, user.name, user.age, user.address)

# .all()あり→全件一括取得＝スピード〇、メモリ×
#  →usersの形で、別のプログラムに受け渡すときに使う（ほぼこっち）。
# .all()なし→１行ずつ取得＝スピード×、メモリ〇
# →データ量がものすごい多い（何千、何万の）ときに使う。
# ※別件、こっち(.all()なし)はsessionのwith文の中で用いる縛りがある。
# memo: 遅延closeや、クエリの遅延評価などで、with文の外でも動いてしまう
# ことがあるが、これはたまたまなのでNG。

# .first で、最初の1行のみ取得        -> 1 BARIS pertama aje
user = session.query(User).first()
print(user.id, user.name, user.age, user.address)

# .scalarで、スカラー（単一）値取得   -> 1 UNIT aje
count = session.query(func.count(User.id)).scalar()
print(count)

# COUNT(*)は↓
count = session.query(func.count('*')).scalar()
print(count)

# .limitで、取得件数制限
users = session.query(User).limit(3).all()   # 一括取得の.allは最後に記述！
for user in users:
  print(user.id, user.name, user.age, user.address)

# .limit().offset()で、途中＆取得件数制限
users = session.query(User).limit(3).offset(1).all()
for user in users:
  print(user.id, user.name, user.age, user.address)

# 列指定取得
for user in session.query(User.id, User.age).all():
  print(user.id, user.age)

# .filterで条件指定
for user in session.query(User).filter(User.id == 2).all():
  print(user.id, user.name, user.age, user.address)

# AND
for user in session.query(User).filter(User.name == 'b', User.id == 4).all():
  print(user.id, user.name, user.age, user.address)

# OR
for user in session.query(User).filter(or_(User.name == 'b', User.id == 1)).all():
  print(user.id, user.name, user.age, user.address)

# IN
ids = [1, 3, 4]
for user in session.query(User).filter(User.id.in_(ids)).all():
  print(user.id, user.name, user.age, user.address)

# ORDER BY
for user in session.query(User).order_by(desc(User.id)).all():
  print(user.id, user.name, user.age, user.address)

# ORDER BY 2
for user in session.query(User).order_by(desc(User.name), asc(User.id)).all():
  print(user.id, user.name, user.age, user.address)

# ORDER BY + filter
for user in session.query(User).filter(or_(User.id==2, User.id==4)).order_by(desc(User.name), asc(User.id)).all():
  print(user.id, user.name, user.age, user.address)

# 更新
with Session(engine) as session:
  user = session.query(User).filter(User.id == 1).first()
  user.name = 'C'
  session.commit()

# 削除
with Session(engine) as session:
  user = session.query(User).filter(User.id==4).delete()
  session.commit()
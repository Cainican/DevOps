# 03_SQL_Injection.py
from sqlalchemy import create_engine, text
db_path = r'C:\PY23\2025_9_01-2025_9_29\0908_sqlalchemy\user.db'
# engineの作成(DB接続の必要情報定義)
engine = create_engine(
  f'sqlite:///{db_path}',
  echo=True   # 裏で動作しているSQL文を出力する
)

id = '2'
# インジェクションコード
id = '999 OR 1=1'

# select
with engine.connect() as con:
  # セキュリティ上SQL文の文字列連結はダメ
  # sql = text(f"SELECT * FROM user WHERE id = {id}")

  # サニタイジング（無害化）するには、
  # プレースホルダ（仮置き場）(:KeyName)を
  # 利用する
  sql = text("SELECT * FROM user WHERE id = :id")

  # SQL実行 第2引数にて、仮置き場に値をセットする。
  rows = con.execute(sql, {'id': id})

for row in rows:
  print(f'ID:{row.id}, Name:{row.name}, Age:{row.age}')

name = 'a'
# select
with engine.connect() as con:
  # SQL文のルールとして、文字データは
  # 「シングルコーテーション(')」でくくる必要がある。
  # sql = text(f"SELECT * FROM user WHERE name = '{name}'")
  # rows = con.execute(sql)

  # プレースホルダを利用した場合、
  # 文字データを「シングルコーテーション(')」でくくる。
  # のルールは、自動的に行うため、不要。
  # というか、くくると動かない。
  # sql = text("SELECT * FROM user WHERE name=':name'") ←これは動かない。
  sql = text(f"SELECT * FROM user WHERE name=:name")
  rows = con.execute(sql, {'name': name})

  for row in rows:
    print(f'ID:{row.id}, Name:{row.name}, Age:{row.age}')
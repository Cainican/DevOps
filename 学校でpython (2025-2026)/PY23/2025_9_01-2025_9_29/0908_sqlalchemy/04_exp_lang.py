# 04_exp_lang.py
from sqlalchemy import create_engine, text, select, column, literal_column, table
db_path = r'C:\PY23\2025_9_01-2025_9_29\0908_sqlalchemy\user.db'
# engineの作成(DB接続の必要情報定義)
engine = create_engine(
  f'sqlite:///{db_path}',
  echo=True   # 裏で動作しているSQL文を出力する
)

# SQL Expression Language
# 関数によるSQL生成が可能。
# サニタイジングは自動で実施されている。
query = (
  select(
    literal_column('name as a'),    # shimizuめも columnは列名のみ。literalは列名以外もOK
    literal_column('age + 1'),
  )
  .select_from(table('user'))
  # .where(column('age') >= 20)
  .where(column('age') >= 20, column('age') < 100) # カンマ(またはwhere連発)でAND(orも別途importすれば可能)
)

# select
with engine.connect() as con:
  rows = con.execute(query)

print(rows.all())
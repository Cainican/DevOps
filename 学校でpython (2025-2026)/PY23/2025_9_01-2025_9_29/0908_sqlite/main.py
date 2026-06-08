# 0908 sqlite
# SQLite...簡易RDB
# Android, MacOS, Pythonでは
# デフォルトで振り込まれています
import sqlite3

# DB接続
con = sqlite3.connect('2025_9_01-2025_9_29\\0908_sqlite\\sample.db')    # The others wrote '0908_sqlite\\sample.db'

# カーソル取得
cur = con.cursor()

sql = '''\
CREATE TABLE IF NOT EXISTS user(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name STRING
)\
'''

# SQL文の実行
cur.execute(sql)

# commitで確定
con.commit()

# insert
sql = '''\
  INSERT INTO user(
    name
  )
  VALUES('abc')\
'''

# SQL文の実行
cur.execute(sql)

# commitで確定
# con.commit()

# rollbackでキャンセル
con.rollback()

# selectはexecute後
# curで結果を取得する
sql = 'SELECT * FROM user'

# SQL文の実行
cur.execute(sql)

# 抽出系(SELECT)において
# commitとrollbackは不要

# forで存在する行数分
# 繰り返す
for row in cur:
  print(row)
  print(f'ID = {row[0]}, Name = {row[1]}')

# やってみよう3
# 以下のフォーマットで出力
# ID = 1, Name = abc
# ID = 2, Name = abc

# DB切断
con.close()
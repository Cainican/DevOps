##############################
#     課題01-IT11A084-09     #
#   py12_kadai05_ita084_09   #
##############################

# 接続用ライブラリのインポート
import mysql.connector

# MySQLに接続
conn = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "",
	database = "PY12"
)

# カーソルを取得
cursor = conn.cursor()

# クエリ(Query)の作成
select_data_query = "select * from users"

# クエリの実行
cursor.execute(select_data_query)

# 結果を全て取得
rows = cursor.fetchall()

# 結果を表示
for row in rows:
	print("id:",row[0])
	print("name:",row[1])
	print("password:",row[2])

#接続を閉じる
cursor.close()
conn.close()
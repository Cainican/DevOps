##############################
#       課題01-IT11A084      #
#   py12_kadai06_ita084_09   #
##############################

# 接続用ライブラリのインポート
import mysql.connector

# 操作の選択画面
print("課題06 IT11A084 09 エリアッセン カスパ")

while True:
	print("操作を選択してください")
	print("""
		1. ユーザ追加
		2. ユーザ確認
		3. 終了
	""")

	# ユーザ入力を要求
	select_num = int(input("処理を選択: "))

	# 処理の選択
	# ユーザ追加が選ばれた場合
	if select_num == 1:
		# ユーザの追加
		try:
			# 追加するユーザ情報の入力
			user_name = input("ユーザ名: ")
			user_pass = input("パスワード: ")

			# MySQLに接続
			conn = mysql.connector.connect(
				host = "localhost",
				user = "root",
				password = "",
				database = "PY12"
			)

			# カーソルの取得
			cursor = conn.cursor()

			# クエリの作成 (レコードの追加)
			sql = ('insert into users (name, password) values(%s, %s)')

			# 追加するユーザデータの準備
			user_data = [user_name, user_pass]

			# クエリの実行
			cursor.execute(sql, user_data)

			# 結果を認定
			conn.commit()

			print("追加しました!\n")

			# データベースを閉じる
			cursor.close()
			conn.close()

		except OSError as e:
			print(e)
		print("追加に失敗しました\n")

	# MySQLを起動してユーザ追加の動作確認


	if select_num == 2:
		try:
			# 追加するユーザの情報
			userID = input("ID: ")
			userPass = input("PASS: ")

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
			sql = "select * from users"

			# クエリの実行
			cursor.execute(sql)

			# 結果を全て取得
			rows = cursor.fetchall()

			# Input count, so when ID/PASS is correct/incorrect
			# it only shows one "認証OK"/"認証NG", instead of the amount of id's in the database
			cnt = 0

			# 結果を表示
			for row in rows:
				if row[1] == userID and row[2] == userPass:
					print("認証OK\n")

				else:
					cnt += 1

				if cnt == 3:
					print("認証NG\n")

			# 接続を閉じる
			cursor.close()
			conn.close()

		except OSError as e:
			print("e")


	# 終了
	if select_num == 3:
		break
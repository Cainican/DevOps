##############################
#    ユーザ登録のテスト        #
#    register.py             #
#   テキスト：register.txt    #
##############################

#1行入力してみる
#with open("register.txt",mode="w",encoding="utf-8") as w_file:
#	w_file.write("てすと")



#キーボード入力をファイルに書いてみる
with open("register.txt",mode="w",encoding="utf-8") as w_file:
	w_file.write(input("入力: "))





#キーボード入力2つを書いてみる
#続けて入れているので区切りはない
#with open("register.txt",mode="w",encoding="utf-8") as w_file:
#	w_file.write(input("ID: "))
#	w_file.write(input("PWD: "))




#繰り返し入れてみる
#IDがzzzで終了（パスワードは適当に入力）
#with open("register.txt",mode="w",encoding="utf-8") as w_file:
#	while True:
#		id =input("ID: ")
#		pwd = input("PWD: ")
#		if id == "zzz":
#			break
#	w_file.write(id)
#	w_file.write(pwd)

#区切り文字や改行が入らない

#改行を入れてみる
#with open("register.txt",mode="w",encoding="utf-8") as w_file:
#	while True:
#		id =input("ID: ")
#		pwd = input("PWD: ")
#		if id == "zzz":
#			break
#		w_file.write(id)
#		w_file.write(pwd)
#		w_file.write("\n")

#改行されて取り出せるようになった
#IDとPWDをカンマで区切る
#ファイル名：register.csv

#with open("register.csv",mode="w",encoding="utf-8") as w_file:
#	while True:
#		id =input("ID: ")
#		pwd = input("PWD: ")
#		if id == "zzz":
#			break
#		w_file.write(f'{id},{pwd}\n')

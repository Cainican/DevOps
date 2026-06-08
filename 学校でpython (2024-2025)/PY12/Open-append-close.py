# (1) ファイルを開く
a_file = open("test.txt", mode="a", encoding="utf-8")

# (2) ファイルを追記する
a_file.write("昨日から学び、今日を生き、\n")
a_file.write("明日へ期得しよう。\n")
a_file.write("・アルベルト・アインシュタイン\n")

# ファイルを閉じる
a_file.close()
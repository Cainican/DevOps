# (1) ファイルを開く

try:
    a_file = open("test.txt", mode="x", encoding="utf-8")
    a_file.write("私は失敗したことがない。\n")
    a_file.write("ただ、一万通りの方法を\n見つけただけだ。\n")

except FileExistsError:
    print("ファイルは既に存在します。")

else:
    a_file.close()
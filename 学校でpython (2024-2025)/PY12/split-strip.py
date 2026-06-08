################################
#    split()とstrip()のテスト   #
#    split-strip.py            #
#   テキスト：split-strip.txt   #
################################

#まとめてファイルを読み込む
#with open("split-strip.txt",encoding="utf-8") as file:
#	a_file = file.read()

#a_fileは文字列型となり、改行文字を含めて出力される
#print(type(a_file))
#print(a_file)





#1行ずつ切ってリストにする
#with open("split-strip.txt",encoding="utf-8") as file:
#	l_file = file.readlines()

#l_fileはリスト型となり、改行文字を含めて1行ずつに区切られる
#print(type(l_file))
#print(l_file)

#print()



#ただし、内容は\nを含めた文字列のため、比較には使えない
#with open("split-strip.txt",encoding="utf-8") as file:
#	l_file = file.readlines()
#print("リストの内容",l_file[0])	
#「CS12,kanehira」が出力されるはず

#文字列「CS12,kanehira」と比較してみる
#if l_file[0] == "CS12,kanehira":
#	print("同じ")
#else:
#	print("違う")

#「違う」とでてしまう→改行(\n)があるから

#1行ずつ区切って出力してみる
#with open("split-strip.txt",encoding="utf-8") as file:
#	l_file = file.readlines()
#print("1行ずつ区切って出力してみる")
#for line in l_file:
#	print(line)

#改行（\n）とprint()の改行で行間が空く
#strip()を使うと両端の余計な情報が消える

#print()
#print("1行読み、余計な改行を消して出力する")
#with open("split-strip.txt",encoding="utf-8") as file:
#	l_file = file.readlines()
#for line in l_file:
#	str = line.strip()
#	print(str)
#	if str == "CS12,kanehira":
#		print("あたり！")
#		break
#文字列の改行は消えて、正しく判定できていることが分かる

#今はカンマ区切り（ID・PWD）のセットのままなので、区切る

with open("split-strip.txt",encoding="utf-8") as file:
	l_file = file.readlines()
for line in l_file:
	str = line.strip()
	#区切り文字（カンマ）で区切ってリストにする
	user = str.split(",")
	print("--------------")
	print(user[0])
	print(user[1])
	print("--------------")

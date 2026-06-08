###################
# 辞書リスト操作演習  #
#  dict-enshu.py  #
###################

#空白の辞書リストを準備(subject_list)
subject_list = {}

#科目記号に「zz」が入るまで繰り返す
while True:
				#科目記号を入れさせる
				sub_name = input("科目記号：")

				#入力が「zz」ではないか？
				if sub_name == "zz":
							#zzなら繰り返し終了
							break
				else:						#zzじゃなかったら
							#得点を入力
							score = int(input("得点："))
							#辞書リストに追加(リスト[key]=value)
							subject_list[sub_name] = score

#60未満の科目記号と点数を抜き出す
#不合格科目まとめ用辞書リスト
f_sub = {}
#subject_listから
#不合格(60未満)を抜き出してf_subへ

for name,score in subject_list.items():
			#得点(score)が60未満だったらf_subへ
			if  score < 60:
					# f_subへコピー
					f_sub[name] = score


print("\n不合格科目リスト")

# f_sub（不合格リスト）を出力する
if  len(f_sub) > 0:
		#不合格科目ありなのでリスト出力
		for  name,score  in  f_sub.items():
					print("{0}\t{1}".format(name,score))
else:
		print("60点未満なし！")






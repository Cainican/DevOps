#############################################
#  復習　円→外貨変換プログラム（関数編）           #
#  exchange_yen_to_foreign_country_def.py   #
#############################################

def exchange(amount,cur_kinds,p_num):
	usd = 143.5
	eur = 159.2
	cny = 20.2
	krw = 0.1
	if p_num == 1:
		if cur_kinds == 1:
			c_amount = amount / usd
		elif cur_kinds == 2:
			c_amount = amount / eur
		elif cur_kinds == 3:
			c_amount = amount / cny
		elif cur_kinds == 4:
			c_amount = amount / krw
	elif p_num == 2:
		if cur_kinds == 1:
			c_amount = amount * usd
		elif cur_kinds == 2:
			c_amount = amount * eur
		elif cur_kinds == 3:
			c_amount = amount * cny
		elif cur_kinds == 4:
			c_amount = amount * krw
	return c_amount

while True:
	print("1.日本円→外貨")	
	print("2.外貨→日本円")
	print("9.終了\n")

	p_num = int(input("処理を選択してください："))

	if p_num == 9:
			break
	print("\n変換する外貨を選択してください。")
	print("""
1.USドル(USD)
2.ユーロ(EUR)
3.元(CNY)
4.ウォン(KRW)
	""")

	cur_kinds = int(input("番号："))

	amount = float(input("金額を入力してください："))
	
	#関数の呼び出し
	c_amount = exchange(amount,cur_kinds,p_num)

	unit1 = "円"

	if cur_kinds == 1:
		unit2 = "ドル"
	elif cur_kinds == 2:
		unit2 = "ユーロ"
	elif cur_kinds == 3:
		unit2 = "元"
	elif cur_kinds == 4:
		unit2 = "ウォン"

	if p_num == 1:
		print("{0}{1}は{2}{3}です。".format(amount,unit1,c_amount,unit2))
	elif p_num == 2:
		print("{0}{1}は{2}{3}です。".format(amount,unit2,c_amount,unit1))

	print()

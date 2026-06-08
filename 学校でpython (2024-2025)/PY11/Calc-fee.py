# aru yuuenchi no nyuujyouryou wo keisansuru puroguramu
# ninsuu no nyuuryoku
children=int(input("kodomo ryoukin (13sai miman) ha nannin?"))
normal=int(input("tuujyouryoukin (13-64sai) ha nannin?"))
elder=int(input("nenpai-sharyoukin(65sai ijyou) ha nannin?"))

# suukei
total_num=children + normal + elder
children_price=children*500
normal_price=normal*1000
elder_price=elder*700
total_price=children_price+normal_price+elder_price

# waribiki taisho ka kakunin -----------(1)
if total_num >=10:
	print("dantai waribiki ga arimasu")
	total_price=total_price*0.8

else:
	print("waribiki ha arimasen")

# kekka wo hyouji
print("kodomoryoukin :{0} nin * 500 = {1} en".format(children,children_price))
print("tuujyouryoukin :{0} nin * 1000 = {1} en".format(normal,normal_price))
print("nenpai-sharyoukin :{0} nin * 700 = {1} en".format(elder,elder_price))
print("goukei: {0} nin {1} en".format(total_num,total_price))
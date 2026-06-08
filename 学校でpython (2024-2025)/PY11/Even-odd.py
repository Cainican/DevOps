##########################################
#   P. 59 guusuu * kisuu wo hanteisuru   #
##########################################

# ki-bo-do kara nyuuryoku wi uketukeru
num=int(input("suuchi nyuuryoku:"))

# num no suuchi ga guusuu nyuuryoku ka kisuu ka wo hanteisuru
# 2 de watta amari ga 0 dattara guusuu, 1 dattara kisuu
# jyouyozan (%) wo riyousuru
#	a % b ha a/b no amari to naru

if num % 2 == 0:
	print(str(num) + "ha guusuudesu.")

else:
	print(str(num) + "ha kisuudesu.")

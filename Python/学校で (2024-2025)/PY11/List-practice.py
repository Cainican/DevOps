########################
#   List-practice.py   #
########################

# mojiretsu wo ireru risuto, (IT11) wo sakuseishi,
# 5 tsu no moji wo nyuuryokushitara shuuryousuru (kanarazu 5 tsu ireru mono to shimasu)

# list no sakusei ()
IT11 = []

while len(IT11) < 5:
	# risuto ni nyuuryoku naiyou wo ireru
	# risuto no tsuika ha, risuto.append(atai)
	IT11.append(input("deta nyuuryoku: "))

# naiyou no kakunin
# print(IT11)

# risuto no kuria
# IT11.clear()
# print(IT11)

# tokutei no youso wo sakujo
# riutome.remove(atai)
# eba, koi, kane, naka, tsuka
# to nyuuryokushi, [eba] wo sakujosuru
# print(IT11) de dousa kakunin

IT11.remove("eba")
print(IT11)

# tokutei no indekusu (kanjikanji) no youso wo shoukyou
# del risutome[indekusu]
# indekusu [1] wo sakujosuru
del IT11[1]
print(IT11)

# deta wo toridasu (pop)
# risutome.pop(indekusu)
# indekusu wo 
# IT11 no saigo
# kunne ikke nå at skrive de sidste kommentar for de to øvre kommentar


print(IT11.pop())
print(IT11)

# risuto he no sonyuu
# (gen deta: eba, koi, kane, naka, tsuka)
# risutome.insert(index,value)

IT11.insert(1,"tsuka")
print(IT11)
# koi, tsuka, kana to detara owari
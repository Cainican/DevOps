###########################################
#   Kadai0404-IT11A084-09-エリアッセン カスパ   #
#   	        Jyankenpo   		  #
###########################################

import random

sentaku=["0", "1", "2"]

while True:
	while True:
		yuuza_sentaku=input("te wo sentaku (guu: 0, choki: 1, paa: 2, 99: shuuryou): ")

		if yuuza_sentaku == "0" or yuuza_sentaku == "1" or yuuza_sentaku == "2" or yuuza_sentaku == "99":
			break
		else:
			print("chanto nyuuryokushitekudasai")

	if yuuza_sentaku == "99":
		print("owari!")
		break

	pc_sentaku=random.choice(sentaku)
	print("pc no sentaku: {0}".format(pc_sentaku))

	if yuuza_sentaku == pc_sentaku:
		print("aiko")

	elif yuuza_sentaku == "0" and pc_sentaku == "1":
		print("anata no kachi!")

	elif yuuza_sentaku == "1" and pc_sentaku == "2":
		print("anata no kachi!")

	elif yuuza_sentaku == "2" and pc_sentaku == "0":
		print("anata no kachi!")
	
	else:
		print("pc no kachi!")
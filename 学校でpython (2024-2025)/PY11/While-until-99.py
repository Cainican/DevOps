#####################################################
#   99 ga nyuuryokusarerumade suuchi wo kasansuru   #
#       goukeichi wo tomeru (99 ha fukamenai)	    #
#                  While-until-99		    #
#####################################################

# goukei keisanyou hensuu no shokka
sum=0

# muge ru-pu
while True:
	# ki-bo-do nyuuryoku
	num=int(input("suuchi wo nyuuryoku (99 de syuuryou):"))

	# nyuuryoku atai ga 99 dattara owari
	if num==99:
		break	# furi kaeshi wo nukeru

	# soudenakereba kasansuru
	sum+=num

# kekka no shutsuryoku
print("goukei ha {0} desu.".format(sum))
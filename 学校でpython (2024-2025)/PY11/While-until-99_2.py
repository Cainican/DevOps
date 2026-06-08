#####################################################
#   99 ga nyuuryokusarerumade suuchi wo kasansuru   #
#	    yuugen ru-pu de sakuseisuru	   	    #
#		While-until-99_2-py		    #
#####################################################

# goukei keisanyou hensuu no shokka
sum=0

# ki-bo-do nyuuryoku
num=int(input("suuchi wo nyuuryoku (99 de syuuryou):"))

# num 99 jya nai aida furi kaesu
while num !=99:		# break tsukaimasen
	sum +=num	# sum ni kasansuru

	# saido nyuuryokusaseru (tsugi no suuchi)
	num=int(input("suuchi wo nyuuryoku (99 de syuuryou):"))

# kekka no shutsuryoku
print("goukei ha {0} desu.".format(sum))
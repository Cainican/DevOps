#####################################################################
#   eigo to suugaku no tensuu wo nyuuryokusi, tomoni 60 ten ijyou   #
#      dattara goukaku, soudenakereba fugoukaku to hyoujisuru.      #
#####################################################################

# ki-bo-do kara eisuu no tokuten nyuuryoku
eng=int(input("eigo nyuuryoku:"))	#int <- str ni ki
math=int(input("suugaku nyuuryoku:"))	#


# gouhi no hantei (sorezore 60 ijyouka)
#if eng>= 60 and math >= 60:
#	print("goukaku")
#else:
#	print("fugoukaku")

# dekita hita ha and tsukawanaide kaitemiyou...



if eng>=60:
	if math>=60:
		print("goukaku")
	else:
		print("fugoukaku")
else:
	print("fugoukaku")

# ryouhou wo shiyou dekimasu
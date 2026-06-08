##########################################
#   Kadai0402-IT11A084-09-エリアッセンカスパ   #
#	  yuuza ID to pasuwaado		 #
##########################################

# ki-bo-do nyuuryoku
yuuzaID="user"
pasuwaado="12345"

while True:
	a=input("yuuza ID:")
	PWD=input("pasuwaado:")

# yuuza me nyuuryoku
	if a == yuuzaID:
		if PWD == pasuwaado:
			print("一致\n")
			print("ninshou!")
			break
		else:
			print("ID mata ha PWD ga chigaimasu.")

	else:
		print("ID mata ha PWD ga chigaimasu.")
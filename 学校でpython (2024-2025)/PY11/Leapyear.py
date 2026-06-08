year=int(input("seireki nannen ? "))

# uruu toshi ka dou ka hantei
is_leap=False

# (1) 4 de ware tara uruu toshi --- (1)
if year % 4==0:
	# (2)  100 de ware tara uruu toshi deha nai --- (2)
	if year % 100==0:
		# (3) 400 de ware tara uruu toshi --- (3)
		if year % 400==0:
			is_leap=True
		else: # ------------------------- (3)
			is_leap=False
	else: # ------------------------------------ (2)
		is_leap=True
else: # ------------------------ (1)
	is_leap=False

# kekka wo hyouji
if is_leap: # ----- (4)
	print("uruu toshi desu")
else:
	print("heinen desu")
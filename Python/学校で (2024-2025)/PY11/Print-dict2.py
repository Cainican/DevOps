######################
#   Print-dict2.py   #
######################

# jishogata no deta (kudamonome to nedan) wo hensuu ni dainyuu
fruits = {"banana": 300, "orenji": 240, "ichigo": 350, "mango": 400}

# jishogata no deta ichi ran wo hyouji
for name, price in fruits.items(): # -----(1)
	# gamen ni shutsuryoku
	s = "{0} ha, {1} en desu".format(name, price)
	print(s)
#####################
#   Print-dict.py   #
#####################

# jishogata no deta (kudamonome to nedan) wo hensuu nu dainyuu
fruits = {"banana": 300, "orenji": 240, "ichigo": 350, "mango": 400}

# jishogata no deta ichi ran wo hyouji
for name in fruits.keys():
	# nedan wo eru
	price = fruits[name]

	# gamen ni shutsuryoku
	s = "{0} ha, {1} en desu.".format(name,price)
	print(s)
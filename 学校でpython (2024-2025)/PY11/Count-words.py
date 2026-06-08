######################
#   Count-words.py   #
#	P. 108	     #
######################

# tango no shutsugenkaisuu wo kaunto
text = """
keep on asking, and it will be given you;
keep on seeking, and you will find;
keep on knocking, and it will be opened to you;
for everyone asking recieves, and everyone seeking finds;
and to everyone knocking, it will be opened.
"""

# tango wo gukiru(oki kaeru)
# tekisuto.replace(okikaemae,okikaego)
text = text.replace(";","") # ;sakujo
text = text.replace(",","") # ,sakujo
text = text.replace(".","") # .sakujo

# slit: wakeru (wakareru)
# kekka ha risuto de kaettekuru
words = text.split()

# tango wo kazoeru (jisho risuto)
counter = {}

# words kara tango wo 1tsu zutsu toridasu
for w in words:
	ws = w.lower()	# komoji ni henkan

	# kishutsu de areba +1
	# kishutsu no tango janai baai ha 1
	if ws in counter:
		# atta baai
		counter[ws] += 1

	else:
		# nakatta baai
		counter[ws] = 1

		# nakatta baai
		counter

# kekka (counter) wo hyouji
for k,v in counter.items():
	print("{0} \t\t {1}".format(k,v))
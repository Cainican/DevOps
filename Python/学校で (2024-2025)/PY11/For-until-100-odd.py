#######################################################
#   1-100 made no kisuu no goukei wo for * continue   #
#   wo tsukatte keisansuru			      #
#######################################################

# kasankeika wo 
sum=0

# kurikaeshita gara kasansuru
for i in range(1,101):
	# kisuu dattara kasansezu, kurikaeshi ni modoru
	if i % 2 == 0:
		continue

	# sum ni kasansuru
	sum += i

# kekka
print("1 kara 100 made no kisuu no goukei ha {0}desu.".format(sum))
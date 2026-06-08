######################
#   List-akaten.py   #
######################

points = [80,40,23,14,29,58]

# 30 tenminman no akaten risuto no sakusei
# akaten (30 miman) kakunouyou sore no risuto wo sakusei
akaten = []

for p in points:
	# p ga 30 tenmimanka?
	if p < 30:

		#akaten risuto ni tsuika
		akaten.append(p)

# 30 miman no tensuu wo hyoujisuru
print(akaten)
#########################
#   Test-input-sum.py   #
#########################

# sora no risuto wo sakuseisuru
points = []

# goukei
sum = 0

# deta kazu
count = 0

# nyuuryoku wo motomeru

p = int(input("1-100 tensuu nyuuryoku (999 de shuuryou): "))

# suuchi nyuuryoku wo shuuryou (999 nyuuryoku) made kurikaesu
while p != 999:
	# risuto he no tsuika
	points.append(p)

	# saido nyuuryoku wo motomeru
	p = int(input("suuchi nyuuryoku: "))

# risuto ni haitte iru atai no goukei no sanshutsu
for score in points:
	sum += score

# heikin no sanshutsu
avg = sum / len(points)

# heikin no hyouji
print("heikin: {0} ten".format(round(avg,2)))
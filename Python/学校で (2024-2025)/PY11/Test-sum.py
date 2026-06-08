####################
#   Test-sum.py    #
#   Test-sum2.py   #
####################

# aru kurasu no kokugo tesuto no tensuu wo risuto ni dainyuu ---(1)
points = [88,76,67,43,79,80,91]

sum_v = 0

# tesuto no goukei wo motomeru --- (2)
#sum_v = 0
#for i in points:	# kuri kaeshi no
#	sum_v += i
#	print(i,"ten wo tashite goukei ha", sum_v)

# heikin wo motomeru --- (3)
#ave_v = sum_v / len(points)	# hani heikin = goukei / tensuu wo kazu
#print("heikin ten ha:", round(ave_v,1), "ten")


# der mangler noget i koden, gennemsnittet kommer ikke ud...
# for i in points:
# # goukei wo motomeru
#	sum_v += i
#	print(i, "ten wo tashite goukei ha", sum_v)



# saiko ten to saitei ten kakunouyou
# sono 1
#mx = -1
#mn = 999

# sono 2
mx = points[0]
mn = points[0]

# konna for demo dekimasuyo
for i in range(len(points)):
	# goukei wo kasan
	sum_v += points[i]
	print(points[i],"ten wo tashi shite goukei ha",sum_v)
	# saiko ten to saitei ten no check, koushin
	if mx < points[i]:
		mx = points[i]

	if mn > points[i]:
		mn = points[i]

# mx= max(points)	demo dekiru
# mn = min(points)	demo dekiru

ave_v = sum_v / len(points)
print()

print("heikin ten ha:", round(ave_v,1), "ten")
print("saiko ten ha:", mx, "ten")
print("saitei ten ha:", mn, "ten")
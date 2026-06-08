#########################################
#   Kadai0503-ITA084-09-エリアッセン カスパ   #
#########################################

res = 0

# suuchi 1 wo nyuuryoku
a = int(input("suuchi 1 wo nyuuryoku: "))

# suuchi 2 wo nyuuryoku
b = int(input("suuchi 2 wo nyuuryoku: "))


for i in range(a,b + 1):
	res += i


print("{0} kara {1} no goukei ha {2} desu.".format(a,b,res))
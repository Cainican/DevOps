###########################################
#   Kadai0403-IT11A084-09-エリアッセン カスパ   #
#   	   suuchi wo nyuuryoku		  #
###########################################


nani = int(input("suuchi wo nyuuryoku: "))
result = 1

for i in range(1, nani + 1):
	result = result * i

print("{0} no kaijou ha {1} desu.".format(nani, result))
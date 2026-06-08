####################################
#   If-elif.py xxsyuu puroguramu   #
####################################

# yu-za- ni nyuuryoku wo motomeru
cat=input("otona•nakanin•kodomo:")

# cat no moji ni yotte ryoukin wo wakeru
if cat=="otona":
	price=7900

elif cat=="nakanin":
	price=6600

elif cat=="kodomo":
	price=4700

else:
	price=-1

# price ga -1 igainara ryoukin wo hyoujisuru
if price !=-1:
	str="ryoukin ha"+str(price)+"en desu"

else:
	str="nyuuryoku era-"
print(str)
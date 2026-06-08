########################################
#   Kadai03-IT11A084-09-エリアッセンカスパ   #
########################################

# suuchi
Good=90
Nice=70
Normal=60
Close=50
Bad=0

# yu-za- ni goukaku ka fugoukaku nyuuryoku wo matomeru
num=int(input("suuchi:"))

if num>=Good:
	print("goukaku! subarashii!")

elif num>=Nice:
	print("goukaku!")

elif num>=Normal:
	print("girigiri goukaku")

elif num>=Close:
	print("girigiri fugoukaku")

elif num>=Bad:
	print("fugoukaku, motto ganbatte!")

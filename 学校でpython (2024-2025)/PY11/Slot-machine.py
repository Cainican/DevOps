#######################
#   Slot-machine.py   #
#######################


import random

# kaunto hensuu no shokka
cnt = 1

# ransuu wo kimeru
rd_num = random.randint(0,1000)

# ataru made kurikaesu
while rd_num != 18:
	# ransuu shutoku shita suuji wo hyoujisuru
	print("\t",rd_num)

	# shikou kaisuu wo +1
	cnt += 1

	# tsugi no ransuu wo shutoku
	rd_num = random.randint(0,1000)

# nankaime de atattaka wo hyoujisuru
print("\t {0} nankaime de attat!".format(cnt))
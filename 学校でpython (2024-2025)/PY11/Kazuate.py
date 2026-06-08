###################################
#   ransuuyou ita kazuate ge-mu   #
#	         kazuate		      #
###################################

# ransuu de suuchi wo kimeru (1-100)
import random
target_num=random.randint(1,100)

# eranda kazu wo shutsuryoku shitemiru
# print(target_num)

# ki-bo-do nyuuryoku no uketsuke
num=int(input("kore to omou suuji nyuuryoku: "))

# atari hantei
while num != target_num:
	# hazurenanode・・・
	if num < target_num:
		print("motto ookiitte!\n")

	else:
		print("motto chiisaitte!\n")

	# tsugi no nyuuryoku no uketsuke
	num = int(input("kore to omou suuji nyuuryoku: "))

# sekai no hyouji
print("seikai!!!")
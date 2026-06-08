###########################
#     Eliassen Casper	  #
#   IT11A084-09-kadai02   #
###########################

print ("IT11A084-09-Casper")

# 1) suuchi wo nyuuryokusaseru
num1=input("suuchi 1 wo nyuuryoku:")		#num 1 ha str

# 2) suuchi 2 wo nyuuryokusaseru
num2=input("suuchi 2 wo nyuuryoku:")		#num 2 ha str

# 3) suuchi 1 (num1) to suuchi 2 (num2) wo kasansuru
sum=int(num1)+int(num2)					#int toshite kasan

# 4) kekka wo shutsuryokusuru
desc="{0} to {1} wo kasanshita kekka ha {2} desu.".format(num1, num2, sum)
print(desc)
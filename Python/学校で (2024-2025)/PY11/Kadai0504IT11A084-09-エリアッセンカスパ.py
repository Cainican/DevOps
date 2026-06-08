#########################################
#   Kadai0504-ITA084-09-エリアッセン カスパ   #
#########################################

x = 1

y = 1

z = 1

# n wo nyuuryoku
n = int(input("n wo nyuuryoku: "))


# r wo nyuuryoku
r = int(input("r wo nyuuryoku: "))

for i in range(1,n + 1):
	x *= i

for i in range(1,r + 1):
	y *= i

for i in range(1,n - r + 1):
	z *= i

v = x/(y*z)

print("{0} ko kara {1} ko wo toru komi awase no kazu ha {2} toori desu.".format(n,r,v))
######################
#   Subtract105.py   #
######################

# nenrei wo watta amari wo nyuuryokusaseru
age1 = int(input("nenrei wo 3 de watta amari: "))

age2 = int(input("nenrei wo 5 de watta amari: "))

age3 = int(input("nenrei wo 7 de watta amari: "))

# atosuu (70, 21, 15) wo kaketa goukei wo motomeru
age_sum = age1 * 70 + age2 * 21 + age3 * 15

# age_sum no amari ga 105 miman to naru made 105 gensan
while age_sum >= 105:
	age_sum -= 105

# kekka (nenrei) wo hyouji
print("anata no nenrei ha {0} sai desune!".format(age_sum))
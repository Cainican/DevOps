# BMI hantei puroguramu
weight=float(input("dairyou(kg) ha ? "))
height=float(input("shinchou(cm) ha ? "))

#BMI no keisan
height=height/100	# m ni ataisu
BMI=weight/(height*height)

# BMI no atai ni oujite kekka wo bunki ---(1)
result=""		# result wo sora ni site oku (shokka)
if BMI<18.5:
	result="ya se gata"

if(18.5<=BMI) and (BMI<25):
	result="futsuu"

if(25<=BMI) and (BMI<30):
	result="himan(kei)"

if BMI>=30:
	result="himan(omo)"

# kekka wo hyouji
print("BMI:",BMI)
print("hantei:",result)
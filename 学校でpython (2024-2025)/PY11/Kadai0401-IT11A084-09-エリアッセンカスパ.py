##########################################
#   Kadai0401-IT11A084-09-エリアッセンカスパ   #
#	       FizzyBuzz		 #
##########################################

# FizzBuzz
#for i in range(1,21):
#	if i % 15 == 0:
#		print("Fizz Buzz")
#		continue
#
#	if i % 3 == 0:
#		print("Fizz")
#		continue
#
#	if i % 5 == 0:
#		print("Buzz")
#		continue
#
#	print(i)


#while True:
#	i=int(input("yuuza nyuuryoku:"))

#	if i % 15 == 0:
#		print("Fizz Buzz")

#	elif i % 3 == 0:
#		print("Fizz")

#	elif i % 5 == 0:
#		print("Buzz")

#	else:
#		print(i)

num=1

while num <=20:
	if (num % 3 == 0) and (num %5 == 0):
		str = "FizzBuzz"

	elif num % 3 == 0:
		str = "Fizz"

	elif num % 5 == 0:
		str = "Buzz"

	else:
		str = num

	print("{0}\t{1}".format(num, str))
	num += 1
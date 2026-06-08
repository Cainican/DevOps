#########################################
#   Kadai0501-IT11A084-09-エリアッセンカスパ  #
#   	        FizzBuzz		#
#########################################

# 1-20 to FizzBuzz
for i in range(1,21):
	if i % 15 == 0:
		print("Fizz Buzz")
		continue

	if i % 3 == 0:
		print("Fizz")
		continue

	if i % 5 == 0:
		print("Buzz")
		continue

	print(i)